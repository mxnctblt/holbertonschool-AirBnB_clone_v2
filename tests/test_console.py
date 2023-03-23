#!/usr/bin/python3
"""Unittest for the console"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import os


class TestConsoleClass(unittest.TestCase):
    """TestConsoleClass"""
    maxDiff = None

    def setUp(self):
        """ condition to test file saving """
        with open("test.json", 'w'):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ destroys created file """
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_executable_file(self):
        """ Check if file have permissions to execute"""
        # Check for read access
        is_read_true = os.access('console.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('console.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('console.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_check_help(self):
        """ Verifies that each command has a help output """
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help create")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help all")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help show")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help destroy")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help update")
            self.assertTrue(len(help_val.getvalue()) > 0)

    def test_create(self):
        """ Test the create function """
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(help_val.getvalue()) > 0)

    def test_show(self):
        """ test show with normal parameters """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
            basemodel_id = val.getvalue()
            self.assertTrue(len(basemodel_id) > 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show BaseModel ' + basemodel_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")

    def test_show_id(self):
        """ Test with id missing """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show BaseModel')
            self.assertTrue(val.getvalue() == "** instance id missing **\n")

    def test_destroy_id(self):
        """ Check if the id is missing """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy BaseModel')
            self.assertTrue(val.getvalue() == "** instance id missing **\n")

    def destroy_working(self):
        """ Checks is destroy methods deletes succesfully an instance """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
            basemodel_id = val.getvalue()
            self.assertTrue(len(basemodel_id) > 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy BaseModel ' + basemodel_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")

    def test_all_fakeclass(self):
        """ Checks if class name exists """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('all FakeClass')
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_all_working(self):
        """ Checks if the method all works correclty """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('all')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_all_trueclass(self):
        """ Checks that the all method works correctly with a class input """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('all BaseModel')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_update(self):
        """ update test working """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
            user_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update BaseModel " + user_id + " name betty")
            HBNBCommand().onecmd("show BaseModel " + user_id)
            self.assertTrue("betty" in val.getvalue())

    def test_user_console(self):
        """ Test the class user with console """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show User " + user_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all User")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update User " + user_id + " name betty")
            HBNBCommand().onecmd("show User " + user_id)
            self.assertTrue("betty" in val.getvalue())
            HBNBCommand().onecmd("destroy User " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show User "+user_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_place_console(self):
        """ Test the class user with console """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create Place")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Place " + user_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all Place")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update Place " + user_id + " name betty")
            HBNBCommand().onecmd("show Place " + user_id)
            self.assertTrue("betty" in val.getvalue())
            HBNBCommand().onecmd("destroy Place " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Place "+user_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_state_console(self):
        """ Test the class user with console """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create State")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show State " + user_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all State")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update State " + user_id + " name betty")
            HBNBCommand().onecmd("show State " + user_id)
            self.assertTrue("betty" in val.getvalue())
            HBNBCommand().onecmd("destroy State " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show State "+user_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_city_console(self):
        """ Test the class user with console """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create City")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show City " + user_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all City")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update City " + user_id + " name betty")
            HBNBCommand().onecmd("show City " + user_id)
            self.assertTrue("betty" in val.getvalue())
            HBNBCommand().onecmd("destroy City " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show City "+user_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_amenity_console(self):
        """ Test the class user with console """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create Amenity")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Amenity " + user_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all Amenity")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update Amenity " + user_id + " name betty")
            HBNBCommand().onecmd("show Amenity " + user_id)
            self.assertTrue("betty" in val.getvalue())
            HBNBCommand().onecmd("destroy Amenity " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Amenity "+user_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_review_console(self):
        """ Test the class user with console """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create Review")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Review " + user_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all Review")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update Review " + user_id + " name betty")
            HBNBCommand().onecmd("show Review " + user_id)
            self.assertTrue("betty" in val.getvalue())
            HBNBCommand().onecmd("destroy Review " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Review "+user_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")
