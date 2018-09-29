package com.tracker.dto;

import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToMany;
import javax.persistence.Table;

@Entity
@Table(name = "TodoList")
public class TodoList {

	@Id
    @Column(name = "list_name")
	private String listName;
	
	@OneToMany(cascade = CascadeType.ALL)
	@JoinColumn(name = "list_name", referencedColumnName = "list_name")
	private List<Task> taskList;

	public String getName() {
		return listName;
	}

	public void setName(String name) {
		this.listName = name;
	}

	public List<Task> getTaskList() {
		return taskList;
	}

	public void setTaskList(List<Task> taskList) {
		this.taskList = taskList;
	}

	@Override
	public String toString() {
		return "TodoList [listName=" + listName + ", taskList=" + taskList + "]";
	}

}
