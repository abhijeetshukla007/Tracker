package com.tracker.dto;

/**
 * @author Abhijeet
 *
 */
public class Response {
	private String message;
	
	private TodoList list;
	
	

	public TodoList getList() {
		return list;
	}

	public void setList(TodoList list) {
		this.list = list;
	}

	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}
	

}
