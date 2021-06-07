#!/usr/bin/env python3
"""
SQLite functions for iCal storage
"""
# Standard Imports
import json
import os
import sqlite3
import sys


filename = sys.argv[1:][0]

with open(filename) as json_file:
	data = json.load(json_file)
	print(data[1].keys())

###############################################################################
# Module-Level Functions
###############################################################################

event_keys = [
	'@odata.etag',
	'id',
	'createdDateTime',
	'lastModifiedDateTime',
	'changeKey',
	'categories',
	'transactionId',
	'originalStartTimeZone',
	'originalEndTimeZone',
	'iCalUId',
	'reminderMinutesBeforeStart',
	'isReminderOn',
	'hasAttachments',
	'subject',
	'bodyPreview',
	'importance',
	'sensitivity',
	'isAllDay',
	'isCancelled',
	'isOrganizer',
	'responseRequested',
	'seriesMasterId',
	'showAs',
	'type',
	'webLink',
	'onlineMeetingUrl',
	'isOnlineMeeting',
	'onlineMeetingProvider',
	'allowNewTimeProposals',
	'isDraft',
	'hideAttendees',
	'recurrence',
	'onlineMeeting',
	'responseStatus',
	'body',
	'start',
	'end',
	'location',
	'locations',
	'attendees',
	'organizer'
]

#######################################
# create an empty file
#######################################
def touch(fname, mode=0o666, dir_fd=None, **kwargs):
	'''create an empty file'''
	flags = os.O_CREAT | os.O_APPEND
	with os.fdopen(os.open(fname, flags=flags, mode=mode, dir_fd=dir_fd)) as fobj:
		os.utime(fobj.fileno() if os.utime in os.supports_fd else fname,
			dir_fd=None if os.supports_fd else dir_fd, **kwargs)


#######################################
# Connects to a specified SQLite database file
#######################################
def get_db():
	"""Connects to the specific database."""
	database_file = sys.argv[1][:-4] + "sqlite3"
	if not os.path.isfile(database_file):
		touch(database_file)
		overwrite_database()
	client_db = sqlite3.connect(database_file)
	client_db.row_factory = sqlite3.Row
	return client_db


#######################################
# Create Calendar Table
#######################################
def create_calendars_table():
	"""Create calendars Table"""
	client_db = get_db()
	# drop the table if it exists
	query = "DROP TABLE IF EXISTS calendars"
	client_db.execute(query, [])
	client_db.commit()

	# create the table
	query = """
CREATE TABLE calendars (
	odata_etag TEXT,
	id TEXT,
	created_date_time TEXT,
	last_modified_date_time TEXT,
	change_key TEXT,
	categories TEXT,
	transaction_id TEXT,
	original_start_time_zone TEXT,
	original_end_time_zone TEXT,
	i_cal_u_id TEXT,
	reminder_minutes_before_start TEXT,
	is_reminder_on TEXT,
	has_attachments TEXT,
	subject TEXT,
	body_preview TEXT,
	importance TEXT,
	sensitivity TEXT,
	is_all_day TEXT,
	is_cancelled TEXT,
	is_organizer TEXT,
	response_requested TEXT,
	series_master_id TEXT,
	show_as TEXT,
	event_type TEXT,
	web_link TEXT,
	online_meeting_url TEXT,
	is_online_meeting TEXT,
	online_meeting_provider TEXT,
	allow_new_time_proposals TEXT,
	is_draft TEXT,
	hide_attendees TEXT,
	recurrence TEXT,
	online_meeting TEXT,
	response_status TEXT,
	body TEXT,
	start TEXT,
	end TEXT,
	location TEXT,
	locations TEXT,
	attendees TEXT,
	organizer TEXT
);
	"""
	client_db.execute(query, [])
	client_db.commit()
	return


#######################################
# Create the initial tables if there are no tables
#######################################
def overwrite_database():
	"""Create the initial tables if there are no tables"""
	# Initialize tables
	create_calendars_table()


#######################################
# Insert calendar entry 
#######################################
def insert_calendar_entry(event):
	"""Insert pull request data"""
	client_db = get_db()
	# Insert the data
	query = """
INSERT INTO
	calendars
VALUES(
	?, ?, ?, ?, ?,
	?, ?, ?, ?, ?,
	?, ?, ?, ?, ?,
	?, ?, ?, ?, ?,
	?, ?, ?, ?, ?,
	?, ?, ?, ?, ?,
	?, ?, ?, ?, ?,
	?, ?, ?, ?, ?,
	?
)
	"""
	row_data = [str(event[key]) for key in event_keys]
	client_db.execute(query, row_data)
	client_db.commit()


def main():
	filename = sys.argv[1:][0]
	with open(filename) as json_file:
		events = json.load(json_file)
		for event in events:
			insert_calendar_entry(event)

main()
