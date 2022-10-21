package model;

public class Contact {
	
	private String contactId;
	private String firstName;
	private String lastName;
	private String address;
	private String phoneNumber;
	
	public Contact(String contactId, String firstName, String lastName, String address, String phoneNumber) {
		
		//validate inputs against requirements
		boolean isValid = validateInput(contactId, 10);
			
		if(isValid) {
			this.contactId = contactId;
		}
		
		isValid = isValid && setContactFirstName(firstName);
		isValid = isValid && setContactLasttName(lastName);
		isValid = isValid && setAddress(address);
		isValid = isValid && setPhoneNumber(phoneNumber);
		
		if(!isValid) {
			throw new IllegalArgumentException("Invalid input");
		}
		
	}
	
	public boolean setContactFirstName(String firstName) {
		boolean isValid = validateInput(firstName, 10);
		
		if(isValid) {
			this.firstName = firstName;
		}
		return isValid;
	}
	
	public boolean setContactLasttName(String lastName) {
		boolean isValid = validateInput(lastName, 10);
		
		if(isValid) {
			this.lastName = lastName;
		}
		return isValid;
	}
	
	public boolean setAddress(String address) {
		boolean isValid = validateInput(address, 20);
		
		if(isValid) {
			this.address = address;
		}

		return isValid;
	}
	
	public boolean setPhoneNumber(String phoneNumber) {
		boolean IsValid = phoneNumber.matches("\\d{10}");
		
		if(IsValid) {
			this.phoneNumber = phoneNumber;
		}
		return IsValid;
	}
	
	public String getContactId() {
		return contactId;
	}
	
	public String getFirstName() {
		return firstName;
	}
	
	public String getLastName() {
		return lastName;
	}
	
	public String getAddress() {
		return address;
	}
	
	public String getPhoneNumber() {
		return phoneNumber;
	}
	
	private boolean validateInput(String item, int length) {
		return (item != null && item.length() <= length);
	}
}
