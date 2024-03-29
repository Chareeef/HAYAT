# Hayat - A Blood Donation Website

![Hayat Landing Page](https://github.com/Chareeef/HAYAT/assets/100241289/bcfe2d1b-7033-4203-b342-64617be11c15)


Welcome to Hayat, a blood donation website developed by a dedicated team of software engineers! Visit our [deployed site](https://hayat-blood-donation.tech) to explore our platform and learn more about our journey in our final project [blog article](https://medium.com/@youssef.charif.h/hayat-a-blood-donation-website-f95c24c2b078?postPublishedType=initial).

## Table of Contents

1. [Introduction](#introduction)
2. [Team and Roles](#team-and-roles)
3. [Main Purpose](#main-purpose)
4. [Technologies Utilized](#technologies-utilized)
5. [Usage](#usage)
6. [Challenges Overcome](#challenges-overcome)
7. [Team Contact](#team-contact)
8. [Licensing](#licensing)

## Introduction <a name="introduction"></a>

Hayat is a blood donation website aimed at streamlining the blood donation process and fostering transparency between blood donors and transfusion centers. Our platform provides an intuitive interface for both donors and transfusion centers to connect and contribute to life-saving efforts.

## Team and Roles <a name="team-and-roles"></a>

- **Youssef Charif Hamidi**: Database modeling and DevOps management.
- **Kenansa Meseret Nigusie**: Flask routes and API endpoints building.
- **Blain Muema**: Front-end development.

## Main Purpose <a name="main-purpose"></a>

Our project, Hayat, is driven by a fundamental mission: revolutionize the blood donation ecosystem by bridging the gap between Blood Donors and Transfusion Centers. Recognizing the critical role these stakeholders play in ensuring access to life-saving blood supplies, we set out to create a platform that fosters robust coordination and accessibility.

At the heart of our endeavor lies the commitment to establish a user-friendly interface that caters to the unique needs of both Transfusion Centers and Donors. For Transfusion Centers, Hayat provides a platform to disseminate vital information such as contact details, location specifics, and real-time blood inventory statistics. By promoting transparency and accessibility, we empower Transfusion Centers to efficiently manage their resources and eventually receive blood donations right when they are needed the most.

Simultaneously, Hayat offers Donors a seamless experience, allowing them to effortlessly locate registered Transfusion Centers in their respective African cities through an intuitive filtering system. With instant access to critical data, including center locations and blood inventory levels, Donors can make informed decisions about when and where to donate. Furthermore, our innovative "Follow" feature enables Donors to track specific Transfusion Centers, facilitating swift responses to urgent blood donation needs.

In essence, Hayat project serves as a catalyst for positive change in the blood donation landscape, leveraging technology to **hopefully save lives and promote community well-being across Africa**.

## Technologies Utilized <a name="technologies-utilized"></a>

Our project harnesses a range of cutting-edge technologies to deliver a robust and scalable solution. These include:

- **Flask**: A lightweight and flexible web framework for Python, providing the foundation for our application's backend logic.
- **HTML/CSS/Jinja/JavaScript**: Essential web technologies utilized to create dynamic and visually appealing user interfaces.
- **MySQL/SQLAlchemy**: A powerful combination for managing our database infrastructure, ensuring efficient data storage and retrieval.
- **Nginx**: A high-performance web server that serves as a critical component of our application's architecture, handling HTTP requests and optimizing resource delivery.
- **Gunicorn**: A WSGI HTTP server for Python web applications, facilitating the deployment of our Flask application in production environments.
- **HAProxy**: A reliable and versatile load balancer that enhances the reliability and scalability of our application by efficiently distributing incoming traffic across multiple servers.
- **ufw (Uncomplicated Firewall)**: A user-friendly command-line tool for managing firewall configurations on Linux systems, providing an additional layer of security for our application infrastructure.
- **unittest**: The built-in Python unit testing framework used to ensure the reliability and functionality of our application's codebase.

## Usage <a name="usage"></a>

Experience Hayat's functionalities firsthand by visiting [hayat-blood-donation.tech](https://hayat-blood-donation.tech). 

### For Donors:
- Search for registered transfusion centers by geographical filtering.
- Follow specific transfusion centers to keep track of their blood bag statistics.

![Transfusion Center Filter](https://github.com/Chareeef/HAYAT/assets/100241289/f5c1d66e-669e-4d45-a9f6-83244f731038)


### For Transfusion Centers:
- Create accounts to provide contact information, location details.
- Monitor blood inventory statistics.

![Transfusion Center Dashboard](https://github.com/Chareeef/HAYAT/assets/100241289/aa58932f-1cb9-473c-b435-b9e70d248c96)


## Challenges Overcome <a name="challenges-overcome"></a>

### User Session Management
We encountered difficulties with user session management, especially with the round-robin load balancing mechanism. This resulted in users losing their logged-in sessions due to requests being routed to different servers. To solve this, we implemented sticky sessions on the load balancer, ensuring consistent user sessions across servers.

### Unique ID Generation
Another challenge was ensuring unique IDs for donors and transfusion centers. Initially, auto-incrementing integers caused conflicts, leading to incorrect user logins. We addressed this by using the shortuuid Python module to generate unique IDs, resolving the issue seamlessly.

## Team Contact <a name="team-contact"></a>

- **Youssef Charif Hamidi** : [GitHub](https://github.com/Chareef) | [LinkedIn](https://linkedin.com/in/youssef-charif-hamidi) | [X](https://x.com/YoussefCharifH2)
- **Blain Muema** : [GitHub](https://github.com/octocatblain) | [LinkedIn](https://linkedin.com/in/blain-muema) | [X](https://twitter.com/birdblain)
- **Kenansa Meseret Nigusie** : [GitHub](https://github.com/Kenc0de) | [LinkedIn](https://linkedin.com/in/kenc0de) | [X](https://twitter.com/KENC0DE)

## Licensing <a name="licensing"></a>

Hayat is licensed under the [MIT License](LICENSE), ensuring its availability for widespread use and modification.

---
**Note:** "Hayat" means "Life" in Arabic, symbolizing the project's mission to contribute to saving lives through blood donation.
