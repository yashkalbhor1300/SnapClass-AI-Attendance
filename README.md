# SnapClass – Smart Attendance System

# 

# SnapClass is an AI-powered attendance management system that uses face recognition to automate classroom attendance. It provides separate Student and Teacher portals with attendance tracking and subject management.

# 

# Features

# Face recognition-based student identification

# Student registration with face enrollment

# Teacher login and registration

# Subject creation and management

# Student enrollment using subject codes

# Classroom photo-based attendance

# Attendance confirmation before saving

# Attendance records and session statistics

# Student attendance history

# Optional voice-based attendance

# Supabase database integration

# Streamlit web interface

# Technologies Used

# Python

# Streamlit

# OpenCV

# dlib

# face recognition

# NumPy

# Pandas

# scikit-learn

# Supabase

# bcrypt

# PIL

# Git \& GitHub

# Project Structure

# SnapClass-AI-Attendance/

# │

# ├── app.py

# ├── requirements.txt

# ├── .gitignore

# │

# ├── src/

# │   ├── components/

# │   ├── database/

# │   ├── pipelines/

# │   ├── screens/

# │   └── ui/

# │

# └── README.md

# How It Works

# Student

# Open the Student Portal.

# Use the camera for face recognition.

# Existing students are identified automatically.

# New students can create a profile using face enrollment.

# Students can enroll in subjects using a subject code.

# Students can view their attendance records.

# Teacher

# Open the Teacher Portal.

# Register or log in.

# Create and manage subjects.

# Share subject codes with students.

# Upload classroom photos.

# Run face recognition to identify students.

# Review the attendance results.

# Confirm and save attendance.

# View attendance records and class statistics.

# Database

# 

# SnapClass uses Supabase for storing:

# 

# Teacher accounts

# Student profiles

# Face embeddings

# Voice embeddings

# Subjects

# Student-subject enrollments

# Attendance records

# Security

# 

# Supabase credentials are stored locally in:

# 

# .streamlit/secrets.toml

# 

# This file is excluded from Git using .gitignore and is not included in the repository.

# 

# Running the Project

# 

# Clone the repository:

# 

# git clone https://github.com/yashkalbhor1300/SnapClass-AI-Attendance.git

# cd SnapClass-AI-Attendance

# 

# Create and activate the required Python environment, install the dependencies, configure the Supabase credentials, and run:

# 

# streamlit run app.py

# Project Highlights

# 

# SnapClass combines computer vision, machine learning, database management, and a Streamlit interface to provide an automated attendance workflow for educational environments.

# 

# Author

# 

# Yash Kalbhor

# 

# B.Tech – Computer Science \& Engineering (AI \& Analytics)

# 

# GitHub: https://github.com/yashkalbhor1300

