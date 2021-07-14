from django.test import Client, TestCase

from .models import Airport, Flight, Passenger


class FlightTestCase(TestCase):
    
    def setUp(self):
        
        #CREATE AIRPORTS
        a1 = Airport.objects.create(code="AAA", city="City A")
        a1 = Airport.objects.create(code="BBB", city="City B")
        
        #CREATE FLIGHTS
        Flight.objects.create(origin=a1, destinantion=a2, duration=100)
        Flight.objects.create(origin=a1, destinantion=a1, duration=200)
        Flight.objects.create(origin=a1, destinantion=a2, duration=100)
        
    def test_departures_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(), 3)
        
    def test_arrivals_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(), 3)

    def test_valid_flight(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        f = Flight.objects.get(origin=a1, destination=a2, duration=100)
        self.assertTrue(f.is_valid_flight())     
        
    def test_invalid_flight_destinantion(self):
        a1 = Airport.objects.get(code="AAA")
        f = Flight.objects.get(origin=a1, destination=a1)
        self.assertFlase(f.is_valid_flight())
        
    def test_invalid_flight_duration(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")    
        f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
        self.assertFlase(f.is_valid_flight())
        
    def test_index(self):
        c = Client()
        response = c.get("/flights/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["flights"].count(), 3)
        