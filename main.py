"""
Main entry point for the Study Assistant
"""

from study_assistant import StudyAssistant
from utils import display_banner, validate_input, save_syllabus

def main():
    """Run the Study Assistant"""
    display_banner()
    
    print("\nWelcome to your personal AI Study Assistant!")
    print("I'll help you create a personalized study plan.\n")
    
    # Get user input
    topic = input("📘 What topic do you want to study? ").strip()
    hours = input("⏱️  How many hours can you dedicate? (default: 10) ").strip()
    level = input("🎓 Your level? (beginner/intermediate/advanced) [default: beginner] ").strip()
    
    # Validate input
    topic, hours, level = validate_input(topic, hours, level)
    
    # Create and run assistant
    assistant = StudyAssistant()
    syllabus = assistant.start_study_session(topic, hours, level)
    
    # Ask if user wants to save
    save_option = input("\n💾 Save this study plan to file? (y/n): ").strip().lower()
    if save_option == 'y':
        filename = input("Enter filename (default: study_plan.txt): ").strip()
        if not filename:
            filename = "study_plan.txt"
        save_syllabus(syllabus, filename)
    
    # Ask if user wants to study another topic
    another = input("\n📚 Study another topic? (y/n): ").strip().lower()
    if another == 'y':
        print("\n" + "="*50)
        main()
    else:
        print("\n👋 Happy learning! Come back anytime you need guidance.")
        print("="*50)

if __name__ == "__main__":
    main()