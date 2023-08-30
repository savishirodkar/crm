# crm

This is a Django project implemented with modular apps for users, agents, teams etc.

Apps
The project contains the following apps:

users - Contains the core user profile and auth models based on AbstractUser.
agents - Agent profile model extending user profile and agent specific functionality.
teams - Models for teams, team members and relationships.
accounts - Custom user account management functionality.
contacts - Models for contacts app, managing leads and customers.
Models
The key models are:

UserProfile (users app) - Custom user model extending AbstractUser
AgentProfile (agents app) - Extends user profile for agent specific fields
Team, TeamMember (teams app) - Models for teams and members
Lead, Customer (contacts app) - Models for leads and customers
Requirements
Python 3.6+
Django 2.2+
Installation
bash



# Clone repo
git clone https://github.com/user/project.git

# Install requirements
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run development server
python manage.py runserver
