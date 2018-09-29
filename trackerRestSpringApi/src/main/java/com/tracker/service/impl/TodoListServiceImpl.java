/**
 * 
 */
package com.tracker.service.impl;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.tracker.dto.Response;
import com.tracker.dto.Task;
import com.tracker.dto.TodoList;
import com.tracker.repo.TodoListRepo;
import com.tracker.service.TodoListService;

/**
 * @author Abhijeet
 *
 */
@Service
public class TodoListServiceImpl implements TodoListService {

	@Autowired
	private TodoListRepo listRepo;

	@Override
	public boolean createTodoList(String listNme) throws Exception {
		TodoList todoList = new TodoList();
		try {
			todoList.setName(listNme);
			todoList.setTaskList(new ArrayList<>());
			listRepo.save(todoList);
			return true;
		} catch (Exception e) {
			return false;
		}

	}

	@Override
	public Optional<TodoList> getListByName(String listName) {
		return listRepo.findById(listName);
	}

	@Override
	public Response addTaskToList(TodoList todoList) throws Exception {
		Response response = new Response();
		try {
			Optional<TodoList> optList = listRepo.findById(todoList.getName());
			String taskToAdd=todoList.getTaskList().get(0).getTaskName();
			if (optList.isPresent()) {
				TodoList list=optList.get();
				boolean taskPresent=  list.getTaskList().stream().anyMatch(entry -> entry.getTaskName().equals(taskToAdd));
				if (taskPresent) {
					response.setMessage("Task " + taskToAdd + "  is already present in list");
				}else {
				response.setMessage("Added task " + taskToAdd + "  to "
						+ todoList.getName() + " list");
				List<Task> taskList=new ArrayList<>();
					taskList.add(todoList.getTaskList().get(0));
				list.getTaskList()
						.add(new Task(todoList.getName(),taskToAdd, new Date()));
				}
				response.setList(list);
				listRepo.save(list);
			} else {
				response.setMessage("Created List " + todoList.getName() + " and added task "
						+ todoList.getTaskList().get(0).getTaskName() + " to list.");
				listRepo.save(todoList);
				response.setList(todoList);
			}
		} catch (Exception e) {
			e.printStackTrace();
			throw new Exception("Error ",e);
		}
		return response;
	}

}
