import unittest
from tests.registration_test import RegistrationTest
from tests.registrtion_test2_FNV import RegistrationTest2FNV
from tests.registration_correct import RegistrationCorrect

# Pobieram testy które chcę uruchomić
registration_test = unittest.TestLoader().loadTestsFromTestCase(RegistrationTest)
registration_test2_FNV = unittest.TestLoader().loadTestsFromTestCase(RegistrationTest2FNV)
registration_correct = unittest.TestLoader().loadTestsFromTestCase(RegistrationCorrect)

# Lista testów
tests_for_run = [
    registration_test,
    registration_test2_FNV,
    registration_correct
]

# Stwórz Test Suitę
test_suite = unittest.TestSuite(tests_for_run)

# Uruchamiam testy
unittest.TextTestRunner().run(test_suite)
