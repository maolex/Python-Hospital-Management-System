class Person:
    def __init__(self, name, age):
        self._name = name  # Encapsulated using a single underscore
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def get_details(self):
        return f"Name: {self._name}, Age: {self._age}"


class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id

    def get_details(self):
        return f"{super().get_details()}, Patient ID: {self.patient_id}"


class Doctor(Person):
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty

    def get_details(self):
        return f"{super().get_details()}, Specialty: {self.specialty}"


class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type

    def get_details(self):
        return f"Room Number: {self.room_number}, Room Type: {self.room_type}"


class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.rooms = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_room(self, room):
        self.rooms.append(room)

    def list_patients(self):
        return [patient.get_details() for patient in self.patients]

    def list_doctors(self):
        return [doctor.get_details() for doctor in self.doctors]

    def list_rooms(self):
        return [room.get_details() for room in self.rooms]

# Example Usage
if __name__ == "__main__":
    hospital = Hospital()
    
    # Add patients
    patient1 = Patient("Bevis Mugabi", 30, "P001")
    patient2 = Patient("Aziz Kayondo", 25, "P002")
    hospital.add_patient(patient1)
    hospital.add_patient(patient2)
    
    # Add doctors
    doctor1 = Doctor("Kenneth Semakula", 40, "Cardiology")
    doctor2 = Doctor("Rashid Watenga", 50, "Neurology")
    hospital.add_doctor(doctor1)
    hospital.add_doctor(doctor2)
    
    # Add rooms
    room1 = Room(101, "Single")
    room2 = Room(102, "Double")
    hospital.add_room(room1)
    hospital.add_room(room2)
    
    # List all patients, doctors, and rooms
    print("Patients:")
    print(hospital.list_patients())
    print("Doctors:")
    print(hospital.list_doctors())
    print("Rooms:")
    print(hospital.list_rooms())
    
    
# Test Suite
import unittest

class TestHospitalManagementSystem(unittest.TestCase):

    def setUp(self):
        self.hospital = Hospital()

    def test_add_patient(self):
        patient = Patient("Alice", 34, "P003")
        self.hospital.add_patient(patient)
        self.assertEqual(len(self.hospital.patients), 1)

    def test_add_doctor(self):
        doctor = Doctor("Dr. Kim", 45, "Orthopedics")
        self.hospital.add_doctor(doctor)
        self.assertEqual(len(self.hospital.doctors), 1)

    def test_add_room(self):
        room = Room(103, "ICU")
        self.hospital.add_room(room)
        self.assertEqual(len(self.hospital.rooms), 1)

    def test_patient_details(self):
        patient = Patient("Bob", 28, "P004")
        self.hospital.add_patient(patient)
        self.assertEqual(patient.get_details(), "Name: Bob, Age: 28, Patient ID: P004")

    def test_doctor_details(self):
        doctor = Doctor("Dr. Smith", 50, "General Practice")
        self.hospital.add_doctor(doctor)
        self.assertEqual(doctor.get_details(), "Name: Dr. Smith, Age: 50, Specialty: General Practice")

    def test_room_details(self):
        room = Room(202, "Suite")
        self.hospital.add_room(room)
        self.assertEqual(room.get_details(), "Room Number: 202, Room Type: Suite")

    def test_list_patients(self):
        self.hospital.add_patient(Patient("Emily", 22, "P005"))
        patients_list = self.hospital.list_patients()
        self.assertIn("Name: Emily, Age: 22, Patient ID: P005", patients_list)

    def test_list_doctors(self):
        self.hospital.add_doctor(Doctor("Dr. Lee", 38, "Pediatrics"))
        doctors_list = self.hospital.list_doctors()
        self.assertIn("Name: Dr. Lee, Age: 38, Specialty: Pediatrics", doctors_list)

    def test_list_rooms(self):
        self.hospital.add_room(Room(104, "Private"))
        rooms_list = self.hospital.list_rooms()
        self.assertIn("Room Number: 104, Room Type: Private", rooms_list)

    def test_multiple_entries(self):
        self.hospital.add_patient(Patient("Jake", 40, "P006"))
        self.hospital.add_doctor(Doctor("Dr. Green", 48, "Oncology"))
        self.hospital.add_room(Room(105, "Single"))
        
        self.assertEqual(len(self.hospital.patients), 1)
        self.assertEqual(len(self.hospital.doctors), 1)
        self.assertEqual(len(self.hospital.rooms), 1)

if __name__ == '__main__':
    unittest.main()