"""
Utility functions for the Study Assistant
"""

def format_time(hours: int) -> str:
    """Format hours into readable time"""
    if hours < 1:
        return f"{hours*60:.0f} minutes"
    elif hours == 1:
        return "1 hour"
    else:
        return f"{hours} hours"

def validate_input(topic: str, hours: str, level: str) -> tuple:
    """Validate and clean user input"""
    # Clean topic
    topic = topic.strip()
    if not topic:
        topic = "Python Programming"
    
    # Validate hours
    try:
        hours = int(hours)
        if hours < 1:
            hours = 10
        elif hours > 100:
            hours = 100
    except:
        hours = 10
    
    # Validate level
    level = level.strip().lower()
    if level not in ["beginner", "intermediate", "advanced"]:
        level = "beginner"
    
    return topic, hours, level

def display_banner():
    """Display welcome banner"""
    banner = """
    ╔══════════════════════════════════════════╗
    ║        🤖 AI STUDY ASSISTANT             ║
    ║        Your Personal Learning Guide      ║
    ╚══════════════════════════════════════════╝
    """
    print(banner)

def save_syllabus(syllabus: dict, filename: str = "study_plan.txt"):
    """Save syllabus to file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"STUDY PLAN: {syllabus['topic']}\n")
        f.write("=" * 50 + "\n\n")
        
        f.write(f"Description: {syllabus['description']}\n")
        f.write(f"Total Hours: {syllabus['total_hours']}\n")
        f.write(f"Level: {syllabus['level']}\n\n")
        
        f.write("MODULES:\n")
        for i, module in enumerate(syllabus['modules'], 1):
            f.write(f"\n{i}. {module['title']} ({module['hours']} hours)\n")
            f.write("   Topics:\n")
            for topic in module['topics']:
                f.write(f"   • {topic}\n")
            f.write("   Exercises:\n")
            for exercise in module['exercises']:
                f.write(f"   • {exercise}\n")
    
    print(f"\n💾 Syllabus saved to {filename}")