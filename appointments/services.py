from datetime import datetime, timedelta

from django.db.models import Q

from .models import Appointment


DEFAULT_SLOT_DURATION = 30


def generate_time_slots(start_time, end_time, slot_duration=DEFAULT_SLOT_DURATION):
    """
    Generate time slots between start and end time
    """

    slots = []

    current = datetime.combine(datetime.today(), start_time)
    end = datetime.combine(datetime.today(), end_time)

    while current + timedelta(minutes=slot_duration) <= end:
        slot_start = current.time()
        slot_end = (current + timedelta(minutes=slot_duration)).time()

        slots.append({
            "start_time": slot_start,
            "end_time": slot_end
        })

        current += timedelta(minutes=slot_duration)

    return slots


def is_slot_available(doctor, date, start_time, end_time):
    """
    Check if doctor has another appointment in the same time
    """

    conflict = Appointment.objects.filter(
        doctor=doctor,
        date=date
    ).filter(
        Q(start_time__lt=end_time) &
        Q(end_time__gt=start_time)
    ).exists()

    return not conflict


def get_booked_slots(doctor, date):
    """
    Return all booked slots for a doctor in a specific date
    """

    return Appointment.objects.filter(
        doctor=doctor,
        date=date
    ).values("start_time", "end_time")


def get_available_slots(doctor, date, work_start, work_end, slot_duration=DEFAULT_SLOT_DURATION):
    """
    Return available time slots for booking
    """

    all_slots = generate_time_slots(work_start, work_end, slot_duration)

    booked = get_booked_slots(doctor, date)

    available = []

    for slot in all_slots:

        conflict = False

        for b in booked:
            if (
                slot["start_time"] < b["end_time"]
                and slot["end_time"] > b["start_time"]
            ):
                conflict = True
                break

        if not conflict:
            available.append(slot)

    return available


def create_appointment(*, doctor, patient, date, start_time, end_time, created_by):
    """
    Create appointment with conflict prevention
    """

    if not is_slot_available(doctor, date, start_time, end_time):
        raise ValueError("This time slot is already booked")

    appointment = Appointment.objects.create(
        doctor=doctor,
        patient=patient,
        date=date,
        start_time=start_time,
        end_time=end_time,
        created_by=created_by
    )

    return appointment


def cancel_appointment(appointment):
    """
    Cancel appointment
    """

    appointment.status = "CANCELLED"
    appointment.save()

    return appointment