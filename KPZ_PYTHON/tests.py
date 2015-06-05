from django.test import TestCase
from models import  PROCESS


class Test (TestCase):
    def create_process (self, NAME, PA, STARTTIME):
        return PROCESS.objects.create(NAME = NAME, PA = PA, STARTTIME = STARTTIME)

    def test_process_creation(self):
        baze = self.create_process('1',1,'2')
        tmp = PROCESS.objects.get(NAME = '1')
        self.assertTrue(isinstance(tmp,PROCESS))
        self.assertEqual(tmp.NAME, baze.NAME)



    def test_select(self):
        self.create_process('_1',1,'2')
        baze = PROCESS.objects.get(NAME = '_1')
        self.assertEqual('_1', baze.NAME)


    def  test_process_insert(self):
        baze = self.create_process(NAME = '11', STARTTIME = 1, PA = '2')
        self.assertEqual(baze, PROCESS.objects.get(NAME = '11'))

    def  test_proc_update(self):
        self.create_process(NAME = '123', STARTTIME = 1, PA = '2')
        baze1 = PROCESS.objects.get(NAME = '123')

        self.assertNotEqual('321', baze1.NAME)
        baze1.NAME = '321'
        baze1.save()
        tmp = PROCESS.objects.get(NAME = '321')
        self.assertEqual('321', tmp.NAME)


    def test_delete (self):
        baze2 = self.create_process('5', 2, '65')
        self.assertIsNotNone(baze2)

        baze2.delete()

        try :
            baze2 = PROCESS.objects.get(NAME = '5')
        except PROCESS.DoesNotExist:
            baze2 = None

        self.assertIsNone(baze2)
