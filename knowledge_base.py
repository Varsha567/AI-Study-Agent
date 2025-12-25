"""
Knowledge base with real curriculum data for common CS topics
"""

TOPIC_KNOWLEDGE = {
    "operating systems": {
        "description": "Software that manages computer hardware and software resources",
        "modules": [
            {
                "title": "Introduction to OS",
                "hours": 2,
                "topics": ["What is OS?", "Types of OS", "OS Architecture", "System Calls"],
                "exercises": ["Install Linux VM", "Explore OS commands"]
            },
            {
                "title": "Process Management",
                "hours": 3,
                "topics": ["Process vs Thread", "CPU Scheduling", "Synchronization", "Deadlocks"],
                "exercises": ["Write multithreaded program", "Simulate scheduling"]
            },
            {
                "title": "Memory Management",
                "hours": 3,
                "topics": ["Memory Allocation", "Virtual Memory", "Paging", "Segmentation"],
                "exercises": ["Memory allocation simulation", "Page replacement algorithms"]
            },
            {
                "title": "File Systems",
                "hours": 2,
                "topics": ["File Organization", "I/O Management", "Disk Scheduling", "File Operations"],
                "exercises": ["File system navigation", "Disk scheduling simulation"]
            }
        ],
        "prerequisites": ["Basic programming", "Computer architecture basics"],
        "resources": ["OS Concepts book", "Coursera OS course", "Linux documentation"]
    },
    
    "python programming": {
        "description": "High-level programming language known for simplicity",
        "modules": [
            {
                "title": "Python Basics",
                "hours": 3,
                "topics": ["Variables & Data Types", "Control Structures", "Functions", "Basic I/O"],
                "exercises": ["Calculator program", "Number guessing game"]
            },
            {
                "title": "Data Structures",
                "hours": 3,
                "topics": ["Lists & Tuples", "Dictionaries", "Sets", "Comprehensions"],
                "exercises": ["Student management system", "Data analysis script"]
            },
            {
                "title": "OOP in Python",
                "hours": 3,
                "topics": ["Classes & Objects", "Inheritance", "Polymorphism", "Encapsulation"],
                "exercises": ["Bank account simulation", "Library management system"]
            },
            {
                "title": "Advanced Topics",
                "hours": 1,
                "topics": ["File Handling", "Error Handling", "Modules & Packages"],
                "exercises": ["File organizer", "Error logging system"]
            }
        ],
        "prerequisites": ["Basic computer usage"],
        "resources": ["Python.org", "W3Schools Python", "Real Python tutorials"]
    },
    
    "machine learning": {
        "description": "Field of AI that enables systems to learn from data",
        "modules": [
            {
                "title": "ML Fundamentals",
                "hours": 3,
                "topics": ["What is ML?", "Types of ML", "Basic terminology", "Applications"],
                "exercises": ["Install Python ML stack", "First ML project"]
            },
            {
                "title": "Supervised Learning",
                "hours": 4,
                "topics": ["Linear Regression", "Logistic Regression", "Decision Trees", "Evaluation Metrics"],
                "exercises": ["House price prediction", "Spam classifier"]
            },
            {
                "title": "Unsupervised Learning",
                "hours": 2,
                "topics": ["Clustering", "Dimensionality Reduction", "Association Rules"],
                "exercises": ["Customer segmentation", "Image compression"]
            },
            {
                "title": "Neural Networks",
                "hours": 1,
                "topics": ["Perceptrons", "Backpropagation", "Deep Learning basics"],
                "exercises": ["MNIST digit recognition", "Simple neural network"]
            }
        ],
        "prerequisites": ["Python programming", "Basic statistics"],
        "resources": ["Scikit-learn documentation", "Kaggle courses", "Andrew Ng's course"]
    }
}

def get_topic_knowledge(topic: str):
    """Get knowledge for a specific topic"""
    topic_lower = topic.lower()
    
    # Check for exact matches
    if topic_lower in TOPIC_KNOWLEDGE:
        return TOPIC_KNOWLEDGE[topic_lower]
    
    # Check for partial matches
    for key in TOPIC_KNOWLEDGE:
        if key in topic_lower or topic_lower in key:
            return TOPIC_KNOWLEDGE[key]
    
    # Return generic template for unknown topics
    return {
        "description": f"Study of {topic}",
        "modules": [
            {
                "title": f"{topic} Basics",
                "hours": 3,
                "topics": ["Fundamental concepts", "Key terminology", "Basic applications"],
                "exercises": ["Practice exercises", "Mini-project"]
            },
            {
                "title": f"Core {topic}",
                "hours": 4,
                "topics": ["Main principles", "Important techniques", "Case studies"],
                "exercises": ["Implementation project", "Problem solving"]
            },
            {
                "title": f"Advanced {topic}",
                "hours": 3,
                "topics": ["Complex scenarios", "Advanced techniques", "Latest developments"],
                "exercises": ["Research project", "Real-world application"]
            }
        ],
        "prerequisites": ["Basic knowledge in the field"],
        "resources": ["Online courses", "Textbooks", "Documentation"]
    }