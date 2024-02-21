# Hayat - A Blood Donation Website

Welcome to Hayat, a blood donation website developed by a dedicated team of software engineers! Visit our [deployed site](https://hayat-blood-donation.tech) to explore our platform and learn more about our journey in our final project [blog article](https://medium.com/@youssef.charif.h/hayat-a-blood-donation-website-f95c24c2b078?postPublishedType=initial).

## Table of Contents

1. [Introduction](#introduction)
2. [Team and Roles](#team-and-roles)
3. [Main Purpose](#main-purpose)
4. [Technologies Used](#technologies-used)
5. [Usage](#usage)
6. [Challenges Overcome](#challenges-overcome)
7. [Team Contact](#team-contact)
8. [Licensing](#licensing)

## Introduction <a name="introduction"></a>

Hayat is a blood donation website aimed at streamlining the blood donation process and fostering transparency between blood donors and transfusion centers. Our platform provides an intuitive interface for both donors and transfusion centers to connect and contribute to life-saving efforts.

## Team and Roles <a name="team-and-roles"></a>

- **Youssef**: Database modeling, DevOps tasks, project management
- **Blain**: Front-end development
- **Ken**: Back-end development

## Main Purpose <a name="main-purpose"></a>

The main purpose of Hayat is to bridge the gap between blood donors and transfusion centers, facilitating easy access to blood donation services and enhancing communication between stakeholders.

## Technologies Used <a name="technologies-used"></a>

- Flask
- HTML/CSS/Jinja/JavaScript
- MySQL/SQLAlchemy
- Nginx
- HAProxy

## Usage <a name="usage"></a>

Experience Hayat's functionalities firsthand by visiting [hayat-blood-donation.tech](https://hayat-blood-donation.tech). 

### For Donors:
- Register as a donor
- Search for registered transfusion centers
- Follow specific transfusion centers to receive updates

### For Transfusion Centers:
- Create accounts to provide contact information, location details, and blood inventory statistics
- Receive donation requests and communicate with donors

## Challenges Overcome <a name="challenges-overcome"></a>

### User Session Management
We encountered difficulties with user session management, especially with the round-robin load balancing mechanism. This resulted in users losing their logged-in sessions due to requests being routed to different servers. To solve this, we implemented sticky sessions on the load balancer, ensuring consistent user sessions across servers.

### Unique ID Generation
Another challenge was ensuring unique IDs for donors and transfusion centers. Initially, auto-incrementing integers caused conflicts, leading to incorrect user logins. We addressed this by using the shortuuid Python module to generate unique IDs, resolving the issue seamlessly.

## Team Contact <a name="team-contact"></a>

- **Youssef Charif Hamidi** : [GitHub](https://github.com/Chareef) | [LinkedIn](https://linkedin.com/in/youssef-charif-hamidi) | [X](https://x.com/YoussefCharifH2)
- **Blain Muema** : [GitHub](https://github.com/octocatblain) | [X](https://twitter.com/birdblain)
- **Kenansa Meseret** : [GitHub](https://github.com/Kenc0de) | [X](https://twitter.com/KENC0DE)

## Licensing <a name="licensing"></a>

Hayat is licensed under the [MIT License](LICENSE), ensuring its availability for widespread use and modification.

---
**Note:** "Hayat" means "Life" in Arabic, symbolizing the project's mission to contribute to saving lives through blood donation.
