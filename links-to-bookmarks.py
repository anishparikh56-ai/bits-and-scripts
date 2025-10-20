import webbrowser
import sys

# Free Learning Resources for Python, Linux, Databases, and C/C++ (113 total - 13 original + 100 new)
resources = [
    # Original 13
    {"name": "Python.org Tutorial", "url": "https://docs.python.org/3/tutorial/", "category": "Python", "description": "Official Python guide for beginners."},
    {"name": "freeCodeCamp Python", "url": "https://www.freecodecamp.org/learn/scientific-computing-with-python/", "category": "Python", "description": "Interactive Python projects and tutorials."},
    {"name": "Codecademy Python 3", "url": "https://www.codecademy.com/learn/learn-python-3", "category": "Python", "description": "Hands-on Python coding exercises."},
    {"name": "CS50 Python Course", "url": "https://cs50.harvard.edu/python/2022/", "category": "Python", "description": "Harvard's intro to Python programming."},
    {"name": "Linux Journey", "url": "https://linuxjourney.com/", "category": "Linux", "description": "Interactive Linux command-line tutorials."},
    {"name": "OverTheWire Wargames", "url": "https://overthewire.org/wargames/", "category": "Linux", "description": "Game-based Linux command challenges."},
    {"name": "Linux Command", "url": "https://linuxcommand.org/", "category": "Linux", "description": "Practical guide to Linux shell scripting."},
    {"name": "freeCodeCamp SQL", "url": "https://www.freecodecamp.org/learn/relational-database/", "category": "Databases", "description": "Learn SQL with hands-on projects."},
    {"name": "W3Schools SQL", "url": "https://www.w3schools.com/sql/", "category": "Databases", "description": "Beginner-friendly SQL tutorials."},
    {"name": "SQLZoo", "url": "https://sqlzoo.net/", "category": "Databases", "description": "Interactive SQL query exercises."},
    {"name": "LearnCpp.com", "url": "https://www.learncpp.com/", "category": "C/C++", "description": "Comprehensive C++ tutorials for all levels."},
    {"name": "C Programming Tutorial", "url": "https://www.cprogramming.com/", "category": "C/C++", "description": "In-depth C programming guides."},
    {"name": "cppreference.com", "url": "https://en.cppreference.com/w/", "category": "C/C++", "description": "C/C++ reference with examples."},
    
    # 100 New Free Resources (Curated from 2025 Sources)
    # Python (40 new)
    {"name": "Rivery Free Python Resources", "url": "https://rivery.io/blog/free-resources-learn-python/", "category": "Python", "description": "9 top free Python learning tools for beginners."},
    {"name": "Hackr.io Python Tutorials", "url": "https://hackr.io/tutorials/learn-python", "category": "Python", "description": "Community-voted Python courses and tutorials."},
    {"name": "Mimo Free Python Guide", "url": "https://mimo.org/blog/how-to-learn-python-for-free-online", "category": "Python", "description": "20 free Python resources including AI tools."},
    {"name": "Udemy Free Python Courses", "url": "https://www.udemy.com/topic/python/free/", "category": "Python", "description": "Free Python training from Udemy experts."},
    {"name": "LearnPython.org Interactive", "url": "https://learnpython.org/", "category": "Python", "description": "Interactive Python tutorial with challenges."},
    {"name": "DEV Community Python Places", "url": "https://dev.to/javinpaul/top-5-places-to-learn-python-programming-for-free-m4c", "category": "Python", "description": "Top 8 free Python websites for 2025."},
    {"name": "Medium Javarevisited Python Sites", "url": "https://medium.com/javarevisited/10-free-python-tutorials-and-courses-from-google-microsoft-and-coursera-for-beginners-96b9ad20b4e6", "category": "Python", "description": "10 free Python tutorials from top providers."},
    {"name": "KDnuggets Free Python Courses", "url": "https://www.kdnuggets.com/10-free-online-courses-to-master-python-in-2025", "category": "Python", "description": "10 free courses to master Python."},
    {"name": "Medium Startup Free Python", "url": "https://medium.com/swlh/5-free-python-courses-for-beginners-to-learn-online-e1ca90687caf", "category": "Python", "description": "15 free Python courses for beginners."},
    {"name": "GitConnected Python Tutorials", "url": "https://gitconnected.com/learn/python", "category": "Python", "description": "Interactive Python tutorials and blogs."},
    {"name": "W3Schools Python", "url": "https://www.w3schools.com/python/", "category": "Python", "description": "Step-by-step Python exercises."},
    {"name": "Intelligent Free Python Classes", "url": "https://www.intelligent.com/best-online-courses/python-classes/", "category": "Python", "description": "Top free Python courses with reviews."},
    {"name": "Python Wiki Beginners", "url": "https://wiki.python.org/moin/BeginnersGuide/Programmers", "category": "Python", "description": "Official Python beginner's guide."},
    {"name": "Kinsta Python Tutorials", "url": "https://kinsta.com/blog/python-tutorials/", "category": "Python", "description": "Best free and paid Python tutorials."},
    {"name": "Real Python Tutorials", "url": "https://realpython.com/", "category": "Python", "description": "In-depth Python articles and videos."},
    {"name": "Python.land Tutorial", "url": "https://python.land/python-tutorial", "category": "Python", "description": "Free beginner Python tutorial with examples."},
    {"name": "GeeksforGeeks Python", "url": "https://www.geeksforgeeks.org/python-programming-language-tutorial/", "category": "Python", "description": "Complete Python tutorial with quizzes."},
    {"name": "Coursera Python Courses", "url": "https://www.coursera.org/courses?query=python", "category": "Python", "description": "Free-to-audit Python courses from universities."},
    {"name": "Analytics Vidhya Free Python", "url": "https://www.analyticsvidhya.com/blog/2024/04/top-free-python-courses/", "category": "Python", "description": "12 free Python courses with certificates."},
    {"name": "Corey Schafer YouTube", "url": "https://www.youtube.com/user/schafer5/playlists", "category": "Python", "description": "Free video tutorials on Python topics."},
    {"name": "Automate the Boring Stuff", "url": "https://automatetheboringstuff.com/", "category": "Python", "description": "Free book on practical Python automation."},
    {"name": "Google Python Class", "url": "https://developers.google.com/edu/python", "category": "Python", "description": "Google's free Python crash course."},
    {"name": "Microsoft Python Intro", "url": "https://learn.microsoft.com/en-us/training/paths/python-language/", "category": "Python", "description": "Free Microsoft Python learning path."},
    {"name": "Khan Academy Python", "url": "https://www.khanacademy.org/computing/computer-programming/programming", "category": "Python", "description": "Interactive Python for beginners."},
    {"name": "Programiz Python", "url": "https://www.programiz.com/python-programming", "category": "Python", "description": "Simple Python tutorial with compiler."},
    {"name": "Tutorialspoint Python", "url": "https://www.tutorialspoint.com/python/index.htm", "category": "Python", "description": "Free Python tutorial with examples."},
    {"name": "Sololearn Python", "url": "https://www.sololearn.com/learning/1076", "category": "Python", "description": "Mobile-friendly free Python course."},
    {"name": "DataCamp Intro Python", "url": "https://www.datacamp.com/courses/intro-to-python-for-data-science", "category": "Python", "description": "Free Python for data science."},
    {"name": "edX Python Basics", "url": "https://www.edx.org/learn/python", "category": "Python", "description": "Free university-level Python courses."},
    {"name": "YouTube freeCodeCamp Python", "url": "https://www.youtube.com/watch?v=rfscVS0vtbw", "category": "Python", "description": "4-hour full Python course."},
    {"name": "Python Crash Course Book", "url": "https://ehmatthes.github.io/pcc_2e/", "category": "Python", "description": "Free online Python book."},
    {"name": "Think Python Book", "url": "https://greenteapress.com/wp/think-python-2e/", "category": "Python", "description": "Free interactive Python textbook."},
    {"name": "Dive Into Python 3", "url": "https://diveintopython3.net/", "category": "Python", "description": "Free advanced Python guide."},
    {"name": "Python for Everybody", "url": "https://www.coursera.org/learn/python", "category": "Python", "description": "Free Coursera Python specialization."},
    {"name": "MIT Python Intro", "url": "https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/", "category": "Python", "description": "MIT's free Python course."},
    {"name": "Numpy Tutorial", "url": "https://numpy.org/doc/stable/user/quickstart.html", "category": "Python", "description": "Free NumPy for scientific computing."},
    {"name": "Pandas Tutorial", "url": "https://pandas.pydata.org/docs/getting_started/intro_tutorials/", "category": "Python", "description": "Free Pandas data manipulation guide."},
    {"name": "Matplotlib Tutorial", "url": "https://matplotlib.org/stable/tutorials/index.html", "category": "Python", "description": "Free plotting with Matplotlib."},
    {"name": "Flask Tutorial", "url": "https://flask.palletsprojects.com/en/3.0.x/tutorial/", "category": "Python", "description": "Free web app building with Flask."},
    {"name": "Django Tutorial", "url": "https://docs.djangoproject.com/en/5.1/intro/tutorial01/", "category": "Python", "description": "Official free Django tutorial."},
    {"name": "Python Discord Community", "url": "https://pythondiscord.com/", "category": "Python", "description": "Free community for Python help."},
    {"name": "Reddit r/learnpython", "url": "https://www.reddit.com/r/learnpython/", "category": "Python", "description": "Free Python learning discussions."},
    # Linux (25 new)
    {"name": "Linux Foundation Resources", "url": "https://training.linuxfoundation.org/resources/", "category": "Linux", "description": "Free Linux courses, webinars, and guides."},
    {"name": "Linux Foundation Free Courses", "url": "https://training.linuxfoundation.org/resources/free-courses/", "category": "Linux", "description": "edX-powered free Linux training."},
    {"name": "Medium Javarevisited Linux CLI", "url": "https://medium.com/javarevisited/top-10-courses-to-learn-linux-command-line-in-2020-best-and-free-f3ee4a78d0c0", "category": "Linux", "description": "Top 10 free Linux CLI courses."},
    {"name": "Hackr.io Linux Courses", "url": "https://hackr.io/blog/best-linux-courses", "category": "Linux", "description": "Best free Linux courses for beginners."},
    {"name": "Triton College Linux Courses", "url": "https://library.triton.edu/c.php?g=1177346&p=8606089", "category": "Linux", "description": "Free online Linux courses list."},
    {"name": "Coursera Linux Courses", "url": "https://www.coursera.org/courses?query=linux", "category": "Linux", "description": "Free-to-audit Linux certifications."},
    {"name": "Udemy Free Linux", "url": "https://www.udemy.com/topic/linux/free/", "category": "Linux", "description": "Free Linux tutorials on Udemy."},
    {"name": "Tecmint Linux Programs", "url": "https://www.tecmint.com/linux-programs-for-students/", "category": "Linux", "description": "Free Linux tools for learning."},
    {"name": "GeeksforGeeks Linux Courses", "url": "https://www.geeksforgeeks.org/blogs/best-linux-online-courses/", "category": "Linux", "description": "Top 10 free Linux courses."},
    {"name": "Class Central Linux", "url": "https://www.classcentral.com/subject/linux", "category": "Linux", "description": "3400+ free Linux courses."},
    {"name": "ItsFoss Free Linux Courses", "url": "https://itsfoss.com/free-linux-training-courses/", "category": "Linux", "description": "14 free Linux and Bash courses."},
    {"name": "Medium Free Linux Resources", "url": "https://medium.com/@shreyashk2498/best-free-resources-to-learn-linux-with-practice-bb2f0c447a5c", "category": "Linux", "description": "Best free Linux practice resources."},
    {"name": "Udemy Linux Topic", "url": "https://www.udemy.com/topic/linux/", "category": "Linux", "description": "Free Linux sysadmin guides."},
    {"name": "Reddit Linux Questions", "url": "https://www.reddit.com/r/linuxquestions/comments/pc2jsy/what_are_the_best_resources_to_learn_linux/", "category": "Linux", "description": "Community free Linux resources."},
    {"name": "PBX Science Linux Path", "url": "https://pbxscience.com/the-best-modern-linux-learning-path/", "category": "Linux", "description": "Modern free Linux learning path."},
    {"name": "Linux Mint Forums Resources", "url": "https://forums.linuxmint.com/viewtopic.php?t=432358", "category": "Linux", "description": "Free books and e-books for Linux."},
    {"name": "edX Linux Essentials", "url": "https://www.edx.org/learn/linux", "category": "Linux", "description": "Free Linux essentials course."},
    {"name": "YouTube Linux Full Course", "url": "https://www.youtube.com/watch?v=6t6DRVSFfTQ", "category": "Linux", "description": "Free 12-hour Linux tutorial."},
    {"name": "OverTheWire Bandit", "url": "https://overthewire.org/wargames/bandit/", "category": "Linux", "description": "Free Linux security challenges."},
    {"name": "TLDP Guides", "url": "https://tldp.org/guides.html", "category": "Linux", "description": "Free Linux Documentation Project guides."},
    {"name": "Arch Linux Wiki", "url": "https://wiki.archlinux.org/title/Beginners%27_guide", "category": "Linux", "description": "Free beginner's guide to Linux."},
    {"name": "Ubuntu Tutorials", "url": "https://ubuntu.com/tutorials", "category": "Linux", "description": "Official free Ubuntu tutorials."},
    {"name": "Fedora Docs", "url": "https://docs.fedoraproject.org/en-US/quick-docs/", "category": "Linux", "description": "Free Fedora quick start guides."},
    {"name": "Debian Handbook", "url": "https://debian-handbook.info/", "category": "Linux", "description": "Free Debian admin handbook."},
    {"name": "Bash Academy", "url": "https://guide.bash.academy/", "category": "Linux", "description": "Free Bash scripting tutorial."},
    # Databases (20 new)
    {"name": "Rivery Free SQL Resources", "url": "https://rivery.io/blog/6-best-free-resources-for-learning-sql/", "category": "Databases", "description": "10 free SQL resources for 2025."},
    {"name": "Udemy Free SQL", "url": "https://www.udemy.com/topic/sql/free/", "category": "Databases", "description": "Free SQL courses on Udemy."},
    {"name": "Estuary Free SQL Guide", "url": "https://estuary.dev/blog/best-free-sql-learning-resources/", "category": "Databases", "description": "11 best free SQL resources."},
    {"name": "Class Central Free SQL", "url": "https://www.classcentral.com/report/best-free-sql-courses/", "category": "Databases", "description": "15 free SQL courses."},
    {"name": "Hackr.io SQL Tutorials", "url": "https://hackr.io/tutorials/learn-sql", "category": "Databases", "description": "Community-recommended free SQL."},
    {"name": "AlmaBetter SQL Tutorial", "url": "https://www.almabetter.com/bytes/tutorials/sql", "category": "Databases", "description": "Free SQL from basics to advanced."},
    {"name": "Hackr.io SQL Courses", "url": "https://hackr.io/blog/best-sql-courses", "category": "Databases", "description": "10 best free SQL courses."},
    {"name": "MLTut Free SQL", "url": "https://www.mltut.com/best-free-sql-courses/", "category": "Databases", "description": "15 free SQL courses with certs."},
    {"name": "Coursera SQL Courses", "url": "https://www.coursera.org/courses?query=sql", "category": "Databases", "description": "Free-to-audit SQL specializations."},
    {"name": "Guru99 Free SQL Certs", "url": "https://www.guru99.com/best-sql-certification-courses.html", "category": "Databases", "description": "8 free SQL courses with certs."},
    {"name": "SQLEasy Interactive SQL", "url": "https://www.sql-easy.com/", "category": "Databases", "description": "Free interactive SQL lessons."},
    {"name": "Codecademy Learn SQL", "url": "https://www.codecademy.com/learn/learn-sql", "category": "Databases", "description": "Free SQL data management course."},
    {"name": "Mimo Best SQL Courses", "url": "https://mimo.org/blog/best-sql-courses", "category": "Databases", "description": "12 best free SQL courses."},
    {"name": "Hackr.io Database Courses", "url": "https://hackr.io/blog/best-database-courses", "category": "Databases", "description": "10 free database courses."},
    {"name": "Placement Prep SQL Sites", "url": "https://www.placementpreparation.io/blog/best-websites-to-learn-sql/", "category": "Databases", "description": "12 free SQL learning sites."},
    {"name": "Airops Free SQL Resources", "url": "https://www.airops.com/blog/learn-sql-for-free-sql-learning-resources", "category": "Databases", "description": "25 free SQL tools and tutorials."},
    {"name": "Javarevisited Free SQL Sites", "url": "https://javarevisited.blogspot.com/2015/06/5-websites-to-learn-sql-online-for-free.html", "category": "Databases", "description": "Top 5 free SQL websites."},
    {"name": "Javarevisited Free SQL Courses", "url": "https://javarevisited.blogspot.com/2019/01/top-6-free-database-and-sql-courses-to-learn-online.html", "category": "Databases", "description": "Top 6 free SQL courses."},
    {"name": "Simplilearn Free SQL", "url": "https://www.simplilearn.com/free-online-course-to-learn-sql-basics-skillup", "category": "Databases", "description": "Free SQL basics with cert."},
    {"name": "Khan Academy SQL", "url": "https://www.khanacademy.org/computing/computer-programming/sql", "category": "Databases", "description": "Free interactive SQL querying."},
    # C/C++ (15 new)
    {"name": "GitConnected C Tutorials", "url": "https://gitconnected.com/learn/c", "category": "C/C++", "description": "Top free interactive C tutorials."},
    {"name": "Great Learning Free C", "url": "https://www.mygreatlearning.com/academy/learn-for-free/courses/c-for-beginners1", "category": "C/C++", "description": "Free C programming with cert."},
    {"name": "Class Central Free C", "url": "https://www.classcentral.com/report/best-free-c-programming-courses/", "category": "C/C++", "description": "10 best free C courses."},
    {"name": "Learn-C.org Interactive", "url": "https://www.learn-c.org/", "category": "C/C++", "description": "Free interactive C tutorial."},
    {"name": "Coursera C Programming", "url": "https://www.coursera.org/courses?query=c%2Bprogramming", "category": "C/C++", "description": "Free C programming paths."},
    {"name": "YouTube C Full Course", "url": "https://www.youtube.com/watch?v=xND0t1pr3KY", "category": "C/C++", "description": "Free 2025 C programming course."},
    {"name": "Coursesity Free C", "url": "https://coursesity.com/free-tutorials-learn/c-programming", "category": "C/C++", "description": "50+ free C courses."},
    {"name": "GeeksforGeeks C Tutorial", "url": "https://www.geeksforgeeks.org/c/c-programming-language/", "category": "C/C++", "description": "Complete free C guide with quizzes."},
    {"name": "W3Schools C", "url": "https://www.w3schools.com/c/", "category": "C/C++", "description": "Free C tutorial with exercises."},
    {"name": "Hackr.io C Tutorials", "url": "https://hackr.io/tutorials/learn-c", "category": "C/C++", "description": "Community-voted free C courses."},
    {"name": "GitConnected C++ Tutorials", "url": "https://gitconnected.com/learn/c-plus-plus", "category": "C/C++", "description": "Top free C++ tutorials."},
    {"name": "GeeksforGeeks Free C++", "url": "https://www.geeksforgeeks.org/blogs/best-free-cpp-courses/", "category": "C/C++", "description": "5 best free C++ courses."},
    {"name": "Medium Javarevisited Free C++", "url": "https://medium.com/javarevisited/top-10-courses-to-learn-c-for-beginners-best-and-free-4afc262a544e", "category": "C/C++", "description": "Free C++ courses for 2025."},
    {"name": "Class Central Free C++", "url": "https://www.classcentral.com/report/best-c-plus-plus-courses/", "category": "C/C++", "description": "10 best free C++ courses."},
    {"name": "Udemy Free C++", "url": "https://www.udemy.com/topic/c-plus-plus/free/", "category": "C/C++", "description": "Free C++ beginner courses."},
    {"name": "Wiingy Free C++ Resources", "url": "https://wiingy.com/resources/best-resources-to-learn-c-plus-plus/", "category": "C/C++", "description": "Best free C++ resources in 2025."},
    {"name": "YouTube C++ 1 Hour", "url": "https://www.youtube.com/watch?v=ZzaPdXTrSb8", "category": "C/C++", "description": "Free 1-hour C++ beginner tutorial."},
    {"name": "SoftwareTestingHelp C++", "url": "https://www.softwaretestinghelp.com/cpp-tutorials/", "category": "C/C++", "description": "70+ free C++ tutorials."},
    {"name": "freeCodeCamp C++", "url": "https://www.youtube.com/watch?v=vLnPwxZdW4Y", "category": "C/C++", "description": "Free full C++ course on YouTube."}
]

def print_banner():
    print("\033[1;36m" + "=" * 80 + "\033[0m")
    print("\033[1;36m" + "     FREE LEARNING RESOURCES (113 TOTAL) FOR PYTHON, LINUX, DBs, C/C++" + "\033[0m")
    print("\033[1;36m" + "=" * 80 + "\033[0m")

def display_resources(resources_list, start=0, page_size=20):
    print("\033[1;32m" + f"ID | Category | Resource Name" + " " * 5 + "| Description" + "\033[0m")
    print("\033[1;32m" + "-" * 80 + "\033[0m")
    end = min(start + page_size, len(resources_list))
    for i in range(start, end):
        global_id = resources.index(resources_list[i]) + 1 if resources_list != resources else i + 1
        print(f"\033[1;33m{global_id:3d}\033[0m | \033[1;35m{resources_list[i]['category']:<8}\033[0m | \033[1;34m{resources_list[i]['name']:<20}\033[0m | {resources_list[i]['description']}")
    if end < len(resources_list):
        print(f"\033[1;33m... Showing {start+1}-{end} of {len(resources_list)}. Type 'n' for more.\033[0m")

def filter_by_category(cat):
    return [r for r in resources if cat.lower() in r['category'].lower()]

def search_by_keyword(keyword):
    return [r for r in resources if keyword.lower() in r['name'].lower() or keyword.lower() in r['description'].lower()]

def open_resource(index):
    if 1 <= index <= len(resources):
        url = resources[index - 1]['url']
        webbrowser.open(url)
        print(f"\033[1;32mOpened: {resources[index - 1]['name']} ({url})\033[0m")
    else:
        print(f"\033[1;31mInvalid ID. Choose 1-{len(resources)}.\033[0m")

if __name__ == "__main__":
    print_banner()
    current_list = resources
    start = 0
    while True:
        display_resources(current_list, start)
        print("\n\033[1;35mOptions: ID to open | 'filter:category' (e.g., filter:Python) | 'search:keyword' | 'n' | 'q' to quit: \033[0m", end="")
        choice = input().strip().lower()
        if choice == 'q':
            print("\033[1;36mExiting... Happy learning!\033[0m")
            sys.exit()
        elif choice.startswith('filter:'):
            cat = choice[7:]
            current_list = filter_by_category(cat)
            start = 0
            if not current_list:
                print("\033[1;31mNo resources found for that category.\033[0m")
                current_list = resources
        elif choice.startswith('search:'):
            kw = choice[7:]
            current_list = search_by_keyword(kw)
            start = 0
            if not current_list:
                print("\033[1;31mNo resources found for that search.\033[0m")
                current_list = resources
        elif choice == 'n' and start + 20 < len(current_list):
            start += 20
        else:
            try:
                idx = int(choice)
                open_resource(idx)
            except ValueError:
                print("\033[1;31mPlease enter a valid option.\033[0m")
