<img src="others/images/purdue-cs-logo.jpg" alt="drawing" width="450"/>

# CS 536: Data Communication and Computer Networks (Fall 2022)

[[_TOC_]]

## Logistics 

- Instructor: [Muhammad Shahbaz](https://mshahbaz.gitlab.io/)
- Teaching assistants:  
  - [Sharuna Anandraj](https://www.linkedin.com/in/sharuna-anandraj-74956313b/)
  - [Darwin Kamanuru](https://www.linkedin.com/in/darwin-k/)
  - [K M A Solaiman](https://www.linkedin.com/in/kmasolaiman/)
  - [Kai Ling](https://keviniling.github.io/)
- Lecture time: **TTh 6:00-7:15pm**
- Location: LYNN 1136
- Credit Hours: 3.00
- Course discussion and announcements: [Campuswire](https://campuswire.com/c/G7E058110/feed)
- Paper reviews: [Perusall](https://app.perusall.com/courses/fall-2022-cs-53600-le1-lec/_/dashboard)
- Project proposal, report, and link to a YouTube video (extra credit): [HotCRP](https://purdue-cs536-fall22.hotcrp.com/)
- Development environment: [AWS Academy](https://awsacademy.instructure.com/courses/24383/pages/cs-536-data-communication-and-computer-networks-fall-2022)
- Exam and assignment submissions: [Gradescope](https://www.gradescope.com/courses/417566)
- Office hours
  - Wednesday 2:00-3:00pm, [Zoom](https://purdue-edu.zoom.us/j/95885631906?pwd=NmhyQXp1dCtYQ09TVFBlRzF3UEYvQT09), Muhammad Shahbaz
  - Tuesday 3:30-4:30pm, [Zoom](https://purdue-edu.zoom.us/j/2489213873), Sharuna Anandraj
  - Thursday 4:00-5:00pm, [Zoom](https://purdue-edu.zoom.us/my/darwk), Darwin Kamanuru
  - Wednesday 3:00-4:00pm, [Zoom](https://purdue-edu.zoom.us/j/93245156625), K M A Solaiman
  - Friday 2:30-3:30pm, [Zoom](https://purdue-edu.zoom.us/j/92496424285), Kai Ling
- Practice study observation (PSO)
  - Wednesday 10:30-11:20am, `BRNG B261`, Sharuna Anandraj
  - Thursday 11:30-12:20pm, `REC 302`, Darwin Kamanuru
  - Wednesday 12:30-1:20pm, `REC 112`, K M A Solaiman
  - Friday 11:30-12:20pm, `UNIV 019`, Kai Ling

> **Note:** Visit [Brightspace](https://purdue.brightspace.com/d2l/home/599158) for instructions on joining [Campuswire](https://campuswire.com/c/G7E058110/feed), [Gradescope](https://www.gradescope.com/courses/417566), [Perusall](https://app.perusall.com/courses/fall-2022-cs-53600-le1-lec/_/dashboard), [HotCRP](https://purdue-cs536-fall22.hotcrp.com/), and [AWS Academy](https://awsacademy.instructure.com/courses/24383/pages/cs-536-data-communication-and-computer-networks-fall-2022).

#### Suggesting edits to the course page and more ...

We strongly welcome any changes, updates, or corrections to the course page or assignments or else that you may have. Please submit them using the [GitLab merge request workflow](https://docs.gitlab.com/ee/development/contributing/merge_request_workflow.html).

## Course Description

CS536 is a graduate-level course in Computer Networks at Purdue University. In this course, we will explore the underlying principles and design decisions that have enabled the Internet to (inter)connect billions of people and trillions of things on and off this planet---especially under the current circumstances marred by COVID-19. We will study the pros and cons of the current Internet design, ranging from classical problems (e.g., packet switching, routing, naming, transport, and congestion control) to emerging and future trends, like data centers, software-defined networking (SDN), programmable data planes, and clound computing to name a few.

The goals for this course are:

- To become familiar with the classical and emerging problems in networking and their solutions.
- To learn what's the state-of-the-art in networking research: network architecture, protocols, and systems.
- To gain practice in reading research papers and critically understanding others' research.
- To gain experience with network programming using state-of-the-art research platforms.

> **Notes:** 
> - This syllabus and schedule is preliminary and subject to change.
> - Everything is due at 11:59 PM (Eastern) on the given day.
> - Abbreviations refer to the following:
>   - PD: Peterson/Davie (online version)
>   - KR: Kurose/Ross (6th edition)
>   - SDN: Peterson/Cascone/O’Connor/Vachuska/Davie (online version)
>   - 5G: Peterson/Sunay (online version)
>   - GV: George Varghese (1st edition)

| Date    | Topics  | Notes | Readings |
| :------ | :------ | :------  | :------ |
| **Week 1** | **ACM SIGCOMM Week** | | |
| Tue, Thu <br> Aug 23, 25 | *[SIGCOMM '22 Conference](https://conferences.sigcomm.org/sigcomm/2022/cfp.html)* <br> No Classes | &bull; How SDN will Shape Networking ([video](https://www.youtube.com/watch?v=c9-K5O_qYgA)) <br> &bull; [Assignment 0](assignments) and [AWS Academy HowTo](https://gitlab.com/purdue-cs536/fall-2022/public/-/raw/main/assignments/cs536-awsacademy-hotwo.pdf.pdf) | &bull; [How to Read a Paper](https://gitlab.com/purdue-cs536/fall-2022/public/-/raw/main/readings/HowToRead2017.pdf) <br> &bull; [Internet History](https://www.internetsociety.org/internet/history-internet/brief-history-internet/) |
| **Week 2** | **Course Overview** | | |
| Tue <br> Aug 30 | Introduction ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/10576026/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5515024&srcou=599158)) | | &bull; [How to Review a Paper](https://greatresearch.org/2013/10/18/the-paper-reviewing-process/) |
| Thu <br> Sep 01 | A Brief History of the Internet ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/10597769/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5536854&srcou=599158)) | &bull; [Paper Review 1](https://app.perusall.com/courses/fall-2022-cs-53600-le1-lec/cerf74-717197892?assignmentId=dWgTv2F8LDcnNnAWB&part=1) `due Sep 13` | &bull; [Research Patterns](https://greatresearch.org/2013/09/20/research-patterns/) (Optional)</li></ul> |
| **Week 3** | **Network Building Blocks** | | |
| Tue <br> Sep 06 | Layering and Protocols I ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/10612215/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5553831&srcou=599158)) | &bull; Team selection for the course project `due Sep 11` | &bull; [End-to-End Arguments](https://gitlab.com/purdue-cs536/fall-2022/public/-/raw/main/readings/e2eArgument84.pdf) |
| Thu <br> Sep 08 | Layering and Protocols II ([video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5563588&srcou=599158)) | &bull; Discuss project ideas and a demo of [Assignment 0](assignments) | &bull; PD: [1.3 (Architecture)](https://book.systemsapproach.org/foundation/architecture.html) |
| **Week 4** | **The Network API** | | |
| Tue <br> Sep 13 | Sockets: The Network Interface ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/10640644/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5584904&srcou=599158)) | &bull; Course Project Proposal `due Oct 04` <br> &bull; [Assignment 1](assignments/assignment1) `due Oct 07` | &bull; PD: [1.4 (Software)](https://book.systemsapproach.org/foundation/software.html) <br> &bull; [Beej's Guide](http://beej.us/guide/bgnet/) (Optional) |
| Thu <br> Sep 15 | Transport: Process-to-Process Communication ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/10659890/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5607038&srcou=599158)) | &bull; [Paper Review 2](https://app.perusall.com/courses/fall-2022-cs-53600-le1-lec/bgpstability98-320363343?assignmentId=QtBqvnHNhZf8LWwWK&part=1) `due Sep 27` | &bull; PD: [2.5 (Reliable Transmission)](https://book.systemsapproach.org/direct/reliable.html) <br> &bull; PD: [5.1 - 5.2 (UDP, TCP)](https://book.systemsapproach.org/e2e.html) |
| **Week 5** | **Local Area Networks** | | |
| Tue <br> Sep 20 | Direct Links: The Wire Interface ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/10674181/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5621207&srcou=599158)) | | &bull; PD: [2.1 - 2.6 (Technology, Encoding, Framing, ...)](https://book.systemsapproach.org/direct.html) |
| Thu <br> Sep 22 | Indirect Links: Internetworking (L2/L3) ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/10682082/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5628928&srcou=599158)) | | &bull; PD: [3 (Internetworking)](https://book.systemsapproach.org/internetworking.html) |
| **Week 6** | **Software Defined Networks** | | |
| Tue <br> Sep 27 | Network Abstractions and Virtualization ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/10707462/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5655913&srcou=599158)) | | &bull; SDN: [3 (Basic Architecture)](https://sdn.systemsapproach.org/arch.html) |
| Thu <br> Sep 29 | Guest Lecture: Open vSwitch Design and the Future by [Ben Pfaff](https://research.vmware.com/researchers/ben-pfaff) ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/10741628/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5655915&srcou=599158)) | &bull; [Paper Review 3](https://app.perusall.com/courses/fall-2022-cs-53600-le1-lec/queue14-709400902?assignmentId=nCeh6yvSMs825XTjE&part=1) `due Oct 13` | &bull; [Open vSwitch (NSDI '15)](https://www.usenix.org/system/files/conference/nsdi15/nsdi15-paper-pfaff.pdf) |
| **Week 7** | **Network Addressing and Configuration** | | |
| Tue <br> Oct 04 | Flat vs Classful vs Classless Addressing ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/10741630/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5690310&srcou=599158)) | | &bull; PD: [3.3.3 - 3.3.9 (Addressing, DHCP ...)](https://book.systemsapproach.org/internetworking.html) |
| Thu <br> Oct 06 | Guest Lecture: Mininet: Fun with Networking and (Lightweight) Virtualization by [Bob Lantz](http://www-cs-students.stanford.edu/~rlantz/) ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/10741631/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5690311&srcou=599158))| | &bull; [A Network in a Laptop (HotNets '10)](https://conferences.sigcomm.org/hotnets/2010/papers/a19-lantz.pdf) |
| **Week 8** | **Datacenter Networks** | | |
| Tue <br> Oct 11 | *October Break* <br> No Class | &bull; [Assignment 2](assignments/assignment2) `due Nov 04` | |
| Thu <br> Oct 13 | Origins and Architectures ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/11225258/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5725746&srcou=599158)) | | &bull; [MapReduce](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf) and an interview with Jeff Dean and Sanjay Ghemawat on why it came into being ([video](https://youtu.be/NXCIItzkn3E)) |
| **Week 9** | **5G & Programmable Networks I** | | |
| Tue <br> Oct 18 | Guest Lecture: Overview of 5G & Aether Platform by [Ajay Thakur](https://www.linkedin.com/in/ajaylthakur/) ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/11239277/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5738009&srcou=599158)) | | &bull; 5G: [3 (Basic Architecture)](https://5g.systemsapproach.org/arch.html) |
| Thu <br> Oct 20 | Guest Lecture: High-speed Programmable Packet Processing and Innovation in Networking by [Vladimir Gurevich](https://www.linkedin.com/in/vladimir-gurevich-63b887/) ([video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5757157&srcou=599158)) | &bull; [Paper Review 4](https://app.perusall.com/courses/fall-2022-cs-53600-le1-lec/rmt-sigcomm13-987183891?assignmentId=G94CTSmT4y9hr89rY&part=1) `due Nov 03` | &bull; SDN: [4 (Bare-Metal Switches)](https://sdn.systemsapproach.org/switch.html) |
| **Week 10** | **Wide Area Networks I** | | |
| Tue <br> Oct 25 | *Midterm Exam* | | |
| Thu <br> Oct 27 | Direct Networks: Intradomain Routing ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/11296986/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5786853&srcou=599158)) | | PD: [3.4 (Routing)](https://book.systemsapproach.org/internetworking/routing.html) |
| **Week 11** | **Wide Area Networks II** | | |
| Tue <br> Nov 01 | Indirect Networks: Interdomain Routing ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/11297002/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5786870&srcou=599158)) | | &bull; PD: [4.1 (Global Internet)](https://book.systemsapproach.org/scaling/global.html) |
| Thu <br> Nov 03 | Indirect Networks: Peering and IXPs ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/11297003/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5786871&srcou=599158)) | | &bull; KR: 4.6.3 (Inter-AS Routing: BGP) <br> &bull; [Where is Internet Congestion Occuring?](https://medium.com/network-insights/where-is-internet-congestion-occurring-e4333ed71168)
| **Week 12** | **Network Diagnostics and Data Persistence** | | |
| Tue <br> Nov 08 | Guest Lecture: How to Diagnose Performance Problems in Networks by [Radhika Mysore](https://research.vmware.com/researchers/radhika-niranjan) ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/11336332/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5822644&srcou=599158)) | &bull; [Paper Review 5](https://app.perusall.com/courses/fall-2022-cs-53600-le1-lec/nsdi18-firestone?assignmentId=SuzCiCYG3bmWiDY7i&part=1) `due Nov 20` | |
| Thu <br> Nov 10 | Guest Lecture: Accelerating Memory and Storage for Datacenter Applications by [Sihang Liu](https://www.sihangliu.com/) ([video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5833292&srcou=599158)) | &bull; [Assignment 3](assignments/assignment3) `due Dec 06` | |
| **Week 13** | **5G & Programmable Networks II** | | |
| Tue <br> Nov 15 | Router Design: Lookup and Scheduling ([ppt](https://purdue.brightspace.com/d2l/le/content/599158/viewContent/11347673/View), [video](https://purdue.brightspace.com/d2l/common/dialogs/quickLink/quickLink.d2l?ou=599158&type=lti&rcode=354644E0-4CD8-419D-A32F-4E78D8778E5C-5833290&srcou=599158)) | | &bull; KR: 4.3 (What's Inside a Router?) <br> &bull; GV: [10 (Exact-Match Lookups), 11 (Prefix-Match Lookups), 13 (Switching)](https://purdue.primo.exlibrisgroup.com/discovery/fulldisplay?docid=alma99169139049601081&context=L&vid=01PURDUE_PUWL:PURDUE&lang=en&search_scope=MyInst_and_CI&adaptor=Local%20Search%20Engine&tab=Everything&query=any,contains,george%20varghese) (Optional) |
| Thu <br> Nov 17 | Guest Lecture: P4 Language and Compiler Design by [Mihai Budiu](https://research.vmware.com/researchers/mihai-budiu) | | |
| **Week 14** | | | |
| Tue <br> Nov 22 | | | |
| Thu <br> Nov 24 | *Thanksgiving Holiday* <br> No Class | | |
| **Week 15** | | | |
| Tue <br> Nov 29 | | | |
| Thu <br> Dec 01 | Project Presentations I | | |
| **Week 16** | | | |
| Tue <br> Dec 06 | Guest Lecture: TBD by [Daniel Firestone](https://www.microsoft.com/en-us/research/people/fstone/) | | |
| Thu <br> Dec 08 | Project Presentations II | | |
| **Week 17** | | | |
| Tue <br> Dec 13 | | | |
| Thu <br> Dec 15 | *Final Exam* | | |

## Prerequisites

This course assumes that students have a basic understanding of data structures and algorithms and experience with programming languages like C/C++ and Python. Please see [CS 240](https://selfservice.mypurdue.purdue.edu/prod/bwckctlg.p_disp_course_detail?cat_term_in=202120&subj_code_in=CS&crse_numb_in=24000), [CS 380](https://selfservice.mypurdue.purdue.edu/prod/bwckctlg.p_disp_course_detail?cat_term_in=202120&subj_code_in=CS&crse_numb_in=38003), or similar courses at Purdue for reference.

## Recommended Textbooks
- Computer Networks: A Systems Approach by L. Peterson and B. Davie ([Online Version](https://book.systemsapproach.org/index.html))
- Computer Networking: A Top-Down Approach by J. Kurose and K. Ross (6th Edition)

> Other optional but interesting resources: 
> - Network Algorithmics: An Interdisciplinary Approach to Designing Fast Networked Devices ([Purdue Library](https://purdue.primo.exlibrisgroup.com/discovery/fulldisplay?docid=alma99169139049601081&context=L&vid=01PURDUE_PUWL:PURDUE&lang=en&search_scope=MyInst_and_CI&adaptor=Local%20Search%20Engine&tab=Everything&query=any,contains,george%20varghese))
> - Software-Defined Networks: A Systems Approach by L. Peterson, C. Cascone, B. O’Connor, T. Vachuska, and Bruce Davie ([Online Version](https://sdn.systemsapproach.org/index.html))
> - 5G Mobile Networks: A Systems Approach by L. Peterson and O. Sunay ([Online Version](https://5g.systemsapproach.org/index.html))
> - TCP Congestion Control: A Systems Approach ([Online Version](https://tcpcc.systemsapproach.org/index.html))
> - Operating an Edge Cloud: A Systems Approach ([Online Version](https://ops.systemsapproach.org))
> - Sytems Approach - [Blog](https://www.systemsapproach.org/blog) 

## Programming Assignments

- [Assignment 0](assignments/assignment0): Virtual networks using Mininet and ONOS `not graded`
- [Assignment 1](assignments/assignment1): File and Message Transmission using Sockets and 3-Way Handshake `due Oct 07`
- [Assignment 2](assignments/assignment2): From Bridging to Switching with VLANs `due Nov 04`
- [Assignment 3](assignments/assignment3): From Bridging to Switching using P4's Match-Action Tables (MATs) `due Dec 06`

## Paper Reading and Discussion

Starting Week 3, we will be reading and discussing **six** research papers on topics ranging from network protocols, systems, and architectures. The class will take place on Thursdays, and we will be discussing one paper every other week -- so we can discuss them in-depth. You should closely read each paper and add comments and questions along with a 1-page summary of the paper on [Perusall](https://app.perusall.com/courses/fall-2022-cs-53600-le1-lec/_/dashboard) by the due date below. Please plan to provide at least five comments or questions for each paper on Perusall ahead of the associated class and follow the comments from other students and the course staff. Please come to class prepared with several points that will substantially contribute to the group discussion. 

> **Note:** General tips on reading papers are [here](https://gitlab.com/purdue-cs536/fall-2022/public/-/raw/main/readings/HowToRead2017.pdf). 

Grades for your class participation and paper reviews will be determined based on attendance and, more importantly, substantial contributions to paper discussions both on Perusall and in class.

> **Note:** 
> - What we expect you to know and prepare before each discussion is [here](readings).
> - Submit paper summaries via [Perusall Notes](https://app.perusall.com/courses/fall-2022-cs-53600-le1-lec/_/notes) and share it with your respective PSO TA and the Professor.

### Reading list
- [Paper 1: A Protocol for Packet Network Intercommunication](https://app.perusall.com/courses/fall-2022-cs-53600-le1-lec/cerf74-717197892?assignmentId=dWgTv2F8LDcnNnAWB&part=1) `due Sep 13`
- [Paper 2: Internet Routing Instability](https://app.perusall.com/courses/fall-2022-cs-53600-le1-lec/bgpstability98-320363343?assignmentId=QtBqvnHNhZf8LWwWK&part=1) `due Sep 27`
- [Paper 3: The Road to SDN: An Intellectual History of Programmable Networks](https://app.perusall.com/courses/fall-2022-cs-53600-le1-lec/queue14-709400902?assignmentId=nCeh6yvSMs825XTjE&part=1) `due Oct 13`
- [Paper 4: Forwarding Metamorphosis: Fast Programmable Match-Action Processing in Hardware for SDN](https://app.perusall.com/courses/fall-2022-cs-53600-le1-lec/rmt-sigcomm13-987183891?assignmentId=G94CTSmT4y9hr89rY&part=1) `due Nov 03`
- [Paper 5: Azure Accelerated Networking: SmartNICs in the Public Cloud](https://app.perusall.com/courses/fall-2022-cs-53600-le1-lec/nsdi18-firestone?assignmentId=SuzCiCYG3bmWiDY7i&part=1) `due Nov 20`
- Paper 6 `TBD`

## Midterm and Final Exams
There will be one midterm and a final exam based on course content (lectures, assignments, and paper readings).

- Midterm Exam `on Oct 25`
- Final Exam `on Dec 15`

> Format: in class, open book

## Course Project

> See a list of past projects [here](https://gitlab.com/purdue-cs536/spring-2021/public/-/tree/master/projects).

The course includes a semester-long systems-building project that should be done in groups (either of size 5 or six, to be determined by the instructor after the course size is finalized) and must involve some programming. All group students are expected to share equally in the implementation. Students are expected to:

1. Reimplement or reproduce results from a paper we read during the semester or on a similar topic OR
2. Implement novel research projects, but such projects must be closely related to the material and topics covered in the course

> **Note:** If you are uncertain about the project's satisfiability, please contact the instructor as soon as possible.

### Project proposal
There are two types of projects in this class: reproducing others' research results and novel research. Proposals should be submitted via [HotCRP](https://purdue-cs536-fall22.hotcrp.com/).

#### a. Reproducing research
For reproducing research projects, students should include the following information in their proposal.

- **Background**
  - Name of the paper
  - A brief summary of the paper's problem domain/challenge, goals, and technical approach
  - Summary of paper's current implementation, evaluation strategy, and key results
- **Plan**
  - Proposed implementation (language, framework, etc.)
  - Evaluation strategy (testing platform/setup, simulated data/traces, etc.)
  - Key results trying to reproduce
  - Discussion of how you can compare your findings (quantitatively, qualitatively) with previously published results
  - New questions/settings trying to evaluate that are not addressed in the original paper
  - As the final plan mentions, it is important when reading a paper to ask what questions and/or settings are not included in an evaluation. For example, what happens if a workload shifts from being uniformly distributed to Zipfian? What if failures occur differently than evaluated? What if the data in a big data processing system has a different structure than evaluated (e.g., the "graph" that the data represents has a different edge distribution)? And so forth ...

#### b. Novel research
For novel research projects, students should include the following information.

- **Background**
  - What problem is research attempting to solve?
  - Why is the problem important?
  - How does this relate directly to topics or papers covered in class
- **Novelty**
  - What is the current state-of-the-art in related work, and why are they insufficient?
  - What is your (novel) technical insight/approach to solving this problem
- **Plan**
  - Proposed implementation (language, framework, etc.)
  - Key questions that evaluation will address
  - Evaluation strategy (testing platform/setup, simulated data/traces, etc.)
  - What does "success" look like? How do you quantify/compare results to alternative approaches / related work?

> **Note:** If students are concerned that their proposed project might not be sufficiently relevant to CS 536 to satisfy the topical criteria, please contact instructors earlier than later. Proposals not closely related to the topical matter may be rejected outright as inappropriate.

### Project selection
The project proposal from above will be finalized. This may involve some back-and-forth between instructors and the group (likely via [Campuswire](https://campuswire.com/c/G7E058110/feed)).

### Final report
The final report will be in the form of a paper written in Latex and submitted as a PDF file via [HotCRP](https://purdue-cs536-fall22.hotcrp.com/).

> **Notes:** 
> - For reproducible projects, the report should have a particular focus and discussion on the evaluation (setup, comparative results, discussion of differences, and so forth).
> - The project writeup should be six pages of double-column, single-spaced, 10-point font (excluding references, which can go on extra pages), similar in spirit to a workshop paper. Papers must be typeset in LaTeX using the [ACM `sigconf` template](https://www.overleaf.com/latex/templates/acm-conference-proceedings-primary-article-template/wbvnghjbzwpc).

### Deliverables

- Team selection `due Sep 11`
- Project proposal `due Oct 04`
- Project report/presentation `TBD`
- Blogpost and/or YouTube video (extra credit) `TBD`

## Grading

- Class participation: 5%
- Programming assignments: 10%
- Paper questions and summaries: 10%
- Midterm exam: 15%
- Final exam: 30%
- Course project: 30% (and 5% extra credit for video/demo posted on YouTube.)

## Policies

### Late submission

- Grace period: 24 hours for the entire semester.
- After the grace period, 25% off for every 24 hours late, rounded up.

If you have extenuating circumstances that result in an assignment being late, please let us know about them as soon as possible.

### Academic integrity

We will default to Purdue's academic policies throughout this course unless stated otherwise. You are responsible for reading the pages linked below and will be held accountable for their contents.
- http://spaf.cerias.purdue.edu/integrity.html
- http://spaf.cerias.purdue.edu/cpolicy.html

### Honor code

By taking this course, you agree to take the [Purdue Honors Pledge](https://www.purdue.edu/odos/osrr/honor-pledge/about.html): "As a boilermaker pursuing academic excellence, I pledge to be honest and true in all that I do. Accountable together - we are Purdue."

### COVID-19 and quarantine + isolation!

Please visit [Protect Purdue Plan](https://protect.purdue.edu/plan/) or [Fall 2022 resources](https://www.purdue.edu/innovativelearning/teaching-remotely/resources.aspx) for most up-to-date guidelines and instructions.

## Acknowledgements

This class borrows inspirations from several incredible sources.

- The final project structure and accompanying instructions are inspired and adapted from my Ph.D. advisor, Jen Rexford's [COS 561](https://www.cs.princeton.edu/courses/archive/fall20/cos461/561.html) class of Fall 2020 at Princeton and Nick McKeown's [CS 244](http://web.stanford.edu/class/cs244/) class at Stanford.
- The lecture slides' material is partially adapted from my Ph.D. advisors, Jen Rexford's [COS 561](https://www.cs.princeton.edu/courses/archive/fall20/cos461/561.html) class and Nick Feamster's [COS 461](https://www.cs.princeton.edu/courses/archive/spring19/cos461/) class at Princeton.
- [Programming assignment 1](assignments/assignment1) is based on a [similar assignment](https://github.com/PrincetonUniversity/COS461-Public/tree/master/assignments/assignment1) offered at Princeton by Nick Feamster.
