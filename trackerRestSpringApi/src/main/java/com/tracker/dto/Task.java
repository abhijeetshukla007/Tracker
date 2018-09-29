package com.tracker.dto;

import java.util.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;

/**
 * @author abhijeet
 *
 */
@Entity
@Table(name = "Task")
public class Task {
	
	public Task() {
		super();
	}

	public Task(String listName, String taskName, Date targetDate) {
		this.listName = listName;
		this.taskName = taskName;
		this.targetDate = targetDate;
	}

	@Id
	@GeneratedValue
	private int id;

	@Column(name = "list_name")
    private String listName;
	
	@Column(name = "task_name")
	private String taskName;

	@Column(name = "target_date")
	private Date targetDate;

	@Column(name = "is_done",columnDefinition = "boolean default false")
	private boolean isDone =false;

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}


	public String getListName() {
		return listName;
	}

	public void setListName(String listName) {
		this.listName = listName;
	}

	public String getTaskName() {
		return taskName;
	}

	public void setTaskName(String taskName) {
		this.taskName = taskName;
	}

	public Date getTargetDate() {
		return targetDate;
	}

	public void setTargetDate(Date targetDate) {
		this.targetDate = targetDate;
	}

	public boolean isDone() {
		return isDone;
	}

	public void setDone(boolean isDone) {
		this.isDone = isDone;
	}

	@Override
	public String toString() {
		return "TaskName ="+ taskName + ", targetDate=" + targetDate
				+ ", isDone=" + isDone;
	}

}