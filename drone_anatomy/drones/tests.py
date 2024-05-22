from django.test import TestCase

from .models import Drone
from .models import DroneImage
from .models import Feature
from .models import Specification


class DroneModelTests(TestCase):
    def test_str_method(self):
        drone = Drone(name="Test Drone", model="Test Model")
        self.assertEqual(str(drone), "Test Drone")

    def test_get_list_url(self):
        self.assertEqual(Drone.get_list_url(), "/drones/")

    def test_get_absolute_url(self):
        drone = Drone(name="Test Drone", model="Test Model")
        self.assertEqual(drone.get_absolute_url(), "/drones/1/")


class FeatureModelTests(TestCase):
    def test_str_method(self):
        feature = Feature(name="Test Feature", description="Test Description")
        self.assertEqual(str(feature), "Test Feature")

    def test_drone_name_property(self):
        drone = Drone(name="Test Drone", model="Test Model")
        feature = Feature(
            name="Test Feature", description="Test Description", drone=drone
        )
        self.assertEqual(feature.drone_name, "Test Drone")

    # def test_drone_url_property(self):
    #     drone = Drone(name='Test Drone', model='Test Model')
    #     feature = Feature(name='Test Feature', description='Test Description', drone=drone)
    #     self.assertEqual(feature.drone_url, drone.get_absolute_url())


class SpecificationModelTests(TestCase):
    def test_str_method(self):
        specification = Specification(name="Test Specification", value="Test Value")
        self.assertEqual(str(specification), "Test Specification: Test Value")


class DroneImageModelTests(TestCase):
    def test_str_method(self):
        drone = Drone(name="Test Drone", model="Test Model")
        drone_image = DroneImage(photo="test.jpg", drone=drone, caption="Test Caption")
        self.assertEqual(str(drone_image), "Test Caption")
