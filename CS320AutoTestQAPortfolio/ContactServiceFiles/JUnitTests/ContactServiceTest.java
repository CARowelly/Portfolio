package test;

import static org.junit.Assert.assertFalse;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import model.Contact;
import service.ContactService;

class ContactServiceTest {

	private static ContactService contactService;
	
	@BeforeAll
	static void setup() {
		contactService = ContactService.getService();
	}
	
	@Test
	void testAddContactSuccess() {
		Contact contact = new Contact("123456", "Bob", "Mike", "1111 E Road Street", "4802929112");	
		assertTrue(contactService.addContact(contact));
		
		Contact getContact = contactService.getContact("123456");
		
		assertTrue(getContact.getContactId().contentEquals(contact.getContactId()));
		assertTrue(getContact.getFirstName().contentEquals(contact.getFirstName()));
		assertTrue(getContact.getLastName().contentEquals(contact.getLastName()));
		assertTrue(getContact.getAddress().contentEquals(contact.getAddress()));
		assertTrue(getContact.getPhoneNumber().contentEquals(contact.getPhoneNumber()));
	}
	
	@Test
	void testAddMultipleContactsSuccess() {
		Contact contact1 = new Contact("123458", "Bob", "Mike", "1111 E Road Street", "4802929112");
		Contact contact2 = new Contact("123459", "Mike", "Mike", "1111 E Road Street", "4802929112");
		
		assertTrue(contactService.addContact(contact1));
		assertTrue(contactService.addContact(contact2));

	}
	
	@Test
	void testAddContactDuplicateIdFail() {
		Contact contact1 = new Contact("123457", "Bob", "Mike", "1111 E Road Street", "4802929112");
		Contact contact2 = new Contact("123457", "Mike", "Mike", "1111 E Road Street", "4802929112");
		
		assertTrue(contactService.addContact(contact1));
		assertFalse(contactService.addContact(contact2));

	}
	
	@Test
	void testGetContactAndUpdateSuccess() {
		Contact contact1 = new Contact("1234", "Bob", "Mike", "1111 E Road Street", "4802929112");

		assertTrue(contactService.addContact(contact1));
		Contact updateContact = contactService.getContact(contact1.getContactId());
		
		updateContact.setPhoneNumber("9421231234");
		updateContact = contactService.getContact(updateContact.getContactId());
		assertTrue(updateContact.getPhoneNumber().equals("9421231234"));
		
	}
	
	@Test
	void testGetContactAndDeleteSuccess() {
		Contact contact1 = new Contact("12", "Bob", "Mike", "1111 E Road Street", "4802929112");

		assertTrue(contactService.addContact(contact1));
		
		Contact contact2 = contactService.getContact(contact1.getContactId());
		assertTrue(contactService.deleteContact(contact2.getContactId()));

		assertTrue(contactService.getContact(contact2.getContactId()) == null);
		
	}
	
	@Test
	void testDeleteInvalidContactFail() {
		String invalidContactId = "1";

		assertFalse(contactService.deleteContact(invalidContactId));
	}

}
