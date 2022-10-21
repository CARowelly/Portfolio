package test;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import model.Contact;

class ContactTest {

	//Test Contact create
	@Test
	void testCreateContactSuccess() {
		Contact contact = new Contact("123456", "Bob", "Mike", "1111 E Road Street", "4802929112");	
		
		assertTrue(contact != null);
		assertTrue(contact.getContactId().equals("123456"));
		assertTrue(contact.getFirstName().equals("Bob"));
		assertTrue(contact.getLastName().equals("Mike"));
		assertTrue(contact.getAddress().equals("1111 E Road Street"));
		assertTrue(contact.getPhoneNumber().equals("4802929112"));
	}
	
	@Test
	void testCreateContactContactIdFails() {
		  Assertions.assertThrows(IllegalArgumentException.class, () -> {
			  new Contact("12345678901", "Bob", "Mike", "1111 E Road Street", "4802929112");
		    });	
	}
	
	@Test
	void testCreateContactFirstNameFails() {
		  Assertions.assertThrows(IllegalArgumentException.class, () -> {
			  new Contact("123456", "Bobbbbbbbbb", "Mike", "1111 E Road Street", "4802929112");
		    });	
	}
	
	@Test
	void testCreateContactLastNameFails() {
		  Assertions.assertThrows(IllegalArgumentException.class, () -> {
			  new Contact("123456", "Bob", "MikeMMMMMMM", "1111 E Road Street", "4802929112");
		    });	
	}
	
	@Test
	void testCreateContactAddressFails() {
		  Assertions.assertThrows(IllegalArgumentException.class, () -> {
			  new Contact("123456", "Bob", "Mike", "1111 E Road Streetttt", "4802929112");
		    });	
	}
	
	@Test
	void testCreateContactNumberToLongFails() {
		  Assertions.assertThrows(IllegalArgumentException.class, () -> {
			  new Contact("123456", "Bob", "Mike", "1111 E Road Streetttt", "48029291123");
		    });	
	}
	
	@Test
	void testCreateContactNumberToShortFails() {
		  Assertions.assertThrows(IllegalArgumentException.class, () -> {
			  new Contact("123456", "Bob", "Mike", "1111 E Road Streetttt", "480292911");
		    });	
	}
	
	
	//Test Contact Update
	
	@Test
	void testUpdateContactSuccess() {
		Contact contact = new Contact("123456", "Bob", "Mike", "1111 E Road Street", "4802929112");	
		
		contact.setAddress("New Address");
		contact.setContactFirstName("Jeff");
		contact.setContactLasttName("Lipson");
		contact.setPhoneNumber("9422222218");
		
		assertTrue(contact.getContactId().equals("123456"));
		assertTrue(contact.getFirstName().equals("Jeff"));
		assertTrue(contact.getLastName().equals("Lipson"));
		assertTrue(contact.getAddress().equals("New Address"));
		assertTrue(contact.getPhoneNumber().equals("9422222218"));
	}
	
	@Test
	void testUpdateContactAddressFails() {
		Contact contact = new Contact("123456", "Bob", "Mike", "1111 E Road Street", "4802929112");	
		assertFalse(contact.setAddress("1111 E Road Streetttt"));
	}
	
	@Test
	void testUpdateContactFirstNameFails() {
		Contact contact = new Contact("123456", "Bob", "Mike", "1111 E Road Street", "4802929112");	
		assertFalse(contact.setContactFirstName("Bobbbbbbbbb"));
	}
	
	@Test
	void testUpdateContactLastNameFails() {
		Contact contact = new Contact("123456", "Bob", "Mike", "1111 E Road Street", "4802929112");	
		assertFalse(contact.setContactLasttName("MikeMMMMMMM"));
	}
	
	@Test
	void testUpdateContactNumberNotDigitFails() {
		Contact contact = new Contact("123456", "Bob", "Mike", "1111 E Road Street", "4802929112");	
		assertFalse(contact.setPhoneNumber("MikeMMMMMMM"));
	}
	
	@Test
	void testUpdateContactNumberToShortFails() {
		Contact contact = new Contact("123456", "Bob", "Mike", "1111 E Road Street", "4802929112");	
		assertFalse(contact.setPhoneNumber("123456"));
	}
	
	@Test
	void testUpdateContactNumberToLongFails() {
		Contact contact = new Contact("123456", "Bob", "Mike", "1111 E Road Street", "4802929112");	
		assertFalse(contact.setPhoneNumber("48029291122"));
	}
	

}
