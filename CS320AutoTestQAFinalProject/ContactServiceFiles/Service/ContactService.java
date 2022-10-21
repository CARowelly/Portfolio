package service;

import java.util.HashMap;
import java.util.Map;

import model.Contact;

public class ContactService {
	
	private static ContactService reference = new ContactService();
	private final Map<String, Contact> contacts;
	
	 ContactService() {
		 this.contacts = new HashMap<String, Contact>();
	 }
	 
		//Create a singleton Contact Service
	 public static ContactService getService() {
		 return reference;
	 }
	 
	 public boolean addContact(Contact contact) {
		 boolean isSuccess = false;
		 
		 if(!contacts.containsKey(contact.getContactId())) {
			 contacts.put(contact.getContactId(), contact);
			 isSuccess = true;
		 }
		 return isSuccess;
	 }
	 
	 public boolean deleteContact(String contactId) {
		 return contacts.remove(contactId) != null;
	 }
	 
	 public Contact getContact(String contactId) {
		 return contacts.get(contactId);
	 }

}
