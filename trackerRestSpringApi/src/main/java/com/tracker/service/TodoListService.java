/**
 * 
 */
package com.tracker.service;

import java.util.Optional;

import com.tracker.dto.Response;
import com.tracker.dto.TodoList;

/**
 * @author Abhijeet
 *
 */
public interface TodoListService {

	boolean createTodoList(String listNme) throws Exception;
	
	Optional<TodoList> getListByName(String listName);

	Response addTaskToList(TodoList todoList) throws Exception;
}
