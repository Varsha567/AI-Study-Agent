"""
Main Study Assistant AI Agent
Combines planning, teaching, and guidance
"""

from syllabus_builder import SyllabusBuilder

class StudyAssistant:
    def __init__(self):
        self.name = "AI Study Assistant"
        self.builder = SyllabusBuilder()
        self.current_syllabus = None
    
    def start_study_session(self, topic: str, hours: int = 10, level: str = "beginner"):
        """Start a complete study session"""
        print(f"\n🤖 {self.name} starting session...")
        print(f"📘 Topic: {topic}")
        print(f"⏱️  Hours: {hours}")
        print(f"🎓 Level: {level}")
        print("=" * 50)
        
        # Step 1: Create syllabus
        self.current_syllabus = self.builder.create_syllabus(topic, hours, level)
        
        # Step 2: Display syllabus
        self._display_syllabus()
        
        # Step 3: Guide through modules
        self._guide_study()
        
        # Step 4: Provide summary
        self._provide_summary()
        
        return self.current_syllabus
    
    def _display_syllabus(self):
        """Display the created syllabus"""
        syllabus = self.current_syllabus
        
        print(f"\n📋 SYLLABUS: {syllabus['topic'].upper()}")
        print("=" * 50)
        print(f"📝 Description: {syllabus['description']}")
        print(f"⏱️  Total Hours: {syllabus['total_hours']}")
        print(f"🎓 Level: {syllabus['level']}")
        
        print(f"\n📚 Prerequisites:")
        for prereq in syllabus['prerequisites']:
            print(f"  • {prereq}")
        
        print(f"\n📖 Modules:")
        for i, module in enumerate(syllabus['modules'], 1):
            print(f"\n  {i}. {module['title']} ({module['hours']} hours)")
            print(f"     📌 Topics to cover:")
            for topic in module['topics']:
                print(f"       • {topic}")
            print(f"     💻 Exercises:")
            for exercise in module['exercises']:
                print(f"       • {exercise}")
        
        print(f"\n📅 Weekly Study Plan:")
        for week in syllabus['study_plan']:
            print(f"\n  Week {week['week']} ({week['hours']} hours):")
            for module in week['modules']:
                print(f"    • {module['title']}")
    
    def _guide_study(self):
        """Guide user through study modules"""
        syllabus = self.current_syllabus
        
        print(f"\n🚀 LET'S START LEARNING!")
        print("=" * 50)
        
        for i, module in enumerate(syllabus['modules'], 1):
            print(f"\n📘 MODULE {i}: {module['title']}")
            print(f"⏱️  Estimated time: {module['hours']} hours")
            print("-" * 40)
            
            # Explain the module
            self._explain_module(module, syllabus['level'])
            
            # Ask if ready to proceed
            if i < len(syllabus['modules']):
                input(f"\n⏭️  Press Enter to continue to next module...")
            else:
                print(f"\n✅ Module completed!")
    
    def _explain_module(self, module: dict, level: str):
        """Explain a module in detail"""
        print(f"\n📚 What you'll learn:")
        for topic in module['topics']:
            print(f"  • {self._explain_topic(topic, level)}")
        
        print(f"\n🎯 Why this matters:")
        print(f"  {self._get_importance(module['title'], level)}")
        
        print(f"\n💡 Learning tips for {level} level:")
        tips = self._get_learning_tips(level)
        for tip in tips:
            print(f"  • {tip}")
        
        print(f"\n💻 Hands-on exercises:")
        for exercise in module['exercises']:
            print(f"  • {exercise}")
        
        print(f"\n❓ Common questions:")
        questions = self._get_common_questions(module['title'])
        for q in questions:
            print(f"  Q: {q['question']}")
            print(f"  A: {q['answer']}")
    
    def _explain_topic(self, topic: str, level: str) -> str:
        """Explain a topic based on level"""
        explanations = {
            "beginner": {
                "process vs thread": "Process is a program in execution, thread is a lightweight process within it",
                "virtual memory": "Makes computer think it has more memory than physically available",
                "paging": "Memory management technique that avoids external fragmentation",
                "linear regression": "Predicts continuous values using a straight line",
                "classes & objects": "Blueprint (class) creates instances (objects) with specific properties"
            }
        }
        
        topic_lower = topic.lower()
        for key in explanations.get(level, {}):
            if key in topic_lower:
                return explanations[level][key]
        
        return topic  # Return as-is if no specific explanation
    
    def _get_importance(self, module_title: str, level: str) -> str:
        """Explain why module is important"""
        importance = {
            "process management": "Essential for understanding how OS manages multiple programs",
            "memory management": "Critical for optimizing computer performance",
            "python basics": "Foundation for all Python programming",
            "supervised learning": "Most common ML approach used in industry"
        }
        
        for key in importance:
            if key in module_title.lower():
                return importance[key]
        
        return "Fundamental for building strong understanding"
    
    def _get_learning_tips(self, level: str) -> list:
        """Get learning tips for the level"""
        tips = {
            "beginner": [
                "Take notes as you learn",
                "Practice with simple examples first",
                "Don't rush - focus on understanding",
                "Ask questions when stuck",
                "Review previous lessons regularly"
            ],
            "intermediate": [
                "Build small projects to apply concepts",
                "Read documentation alongside tutorials",
                "Join study groups or forums",
                "Teach others to reinforce learning",
                "Challenge yourself with complex problems"
            ],
            "advanced": [
                "Read research papers in the field",
                "Contribute to open source projects",
                "Attend conferences or webinars",
                "Mentor beginners",
                "Stay updated with latest developments"
            ]
        }
        
        return tips.get(level, tips["beginner"])
    
    def _get_common_questions(self, module_title: str) -> list:
        """Get common questions for the module"""
        questions_db = {
            "process management": [
                {
                    "question": "What's the difference between process and thread?",
                    "answer": "Process has separate memory space, threads share memory within a process"
                },
                {
                    "question": "What is deadlock?",
                    "answer": "When two or more processes wait for each other indefinitely"
                }
            ],
            "python programming": [
                {
                    "question": "What are Python lists vs tuples?",
                    "answer": "Lists are mutable, tuples are immutable (cannot be changed)"
                },
                {
                    "question": "What is __init__ in Python?",
                    "answer": "Constructor method that initializes object attributes"
                }
            ]
        }
        
        for key in questions_db:
            if key in module_title.lower():
                return questions_db[key]
        
        return [
            {
                "question": "How do I get started?",
                "answer": "Begin with the first exercise and build from there"
            },
            {
                "question": "What if I don't understand something?",
                "answer": "Review the basics, search online, or ask for help"
            }
        ]
    
    def _provide_summary(self):
        """Provide end of session summary"""
        syllabus = self.current_syllabus
        
        print(f"\n" + "=" * 50)
        print(f"🎉 STUDY SESSION COMPLETE!")
        print("=" * 50)
        
        print(f"\n📊 Summary:")
        print(f"  • Topic: {syllabus['topic']}")
        print(f"  • Total hours: {syllabus['total_hours']}")
        print(f"  • Modules completed: {len(syllabus['modules'])}")
        print(f"  • Level: {syllabus['level']}")
        
        print(f"\n📚 Recommended next steps:")
        print(f"  1. Review your notes")
        print(f"  2. Complete all exercises")
        print(f"  3. Build a small project")
        print(f"  4. Teach someone what you learned")
        
        print(f"\n🔗 Useful resources:")
        for resource in syllabus['resources']:
            print(f"  • {resource}")
        
        print(f"\n💪 Keep learning! Consistency is key to mastery.")