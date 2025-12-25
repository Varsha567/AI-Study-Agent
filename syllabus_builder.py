"""
Builds structured syllabus based on topic and hours
"""

from knowledge_base import get_topic_knowledge

class SyllabusBuilder:
    def __init__(self):
        self.name = "Study Assistant"
    
    def create_syllabus(self, topic: str, total_hours: int = 10, level: str = "beginner") -> dict:
        """
        Create a structured syllabus for the given topic
        """
        print(f"\n📝 Creating syllabus for '{topic}'...")
        
        # Get topic knowledge
        knowledge = get_topic_knowledge(topic)
        
        # Adjust based on level
        modules = self._adjust_for_level(knowledge["modules"], level)
        
        # Adjust hours distribution
        modules = self._adjust_hours(modules, total_hours)
        
        # Build syllabus
        syllabus = {
            "topic": topic,
            "description": knowledge["description"],
            "total_hours": total_hours,
            "level": level,
            "prerequisites": knowledge["prerequisites"],
            "resources": knowledge["resources"],
            "modules": modules,
            "study_plan": self._create_study_plan(modules)
        }
        
        return syllabus
    
    def _adjust_for_level(self, modules: list, level: str) -> list:
        """Adjust modules based on user level"""
        adjusted_modules = modules.copy()
        
        if level == "beginner":
            # Simplify for beginners
            for module in adjusted_modules:
                if "advanced" in module["title"].lower():
                    module["hours"] = max(1, module["hours"] - 1)
                # Keep exercises simple
                module["exercises"] = [ex for ex in module["exercises"] if "simple" in ex.lower() or "basic" in ex.lower() or len(module["exercises"]) == 1]
        
        elif level == "advanced":
            # Add complexity for advanced
            for module in adjusted_modules:
                if "advanced" in module["title"].lower():
                    module["hours"] += 1
                module["exercises"].append("Research current trends")
        
        return adjusted_modules
    
    def _adjust_hours(self, modules: list, total_hours: int) -> list:
        """Adjust module hours to match total hours"""
        current_total = sum(module["hours"] for module in modules)
        
        if current_total == total_hours:
            return modules
        
        # Calculate ratio and adjust
        ratio = total_hours / current_total
        for module in modules:
            module["hours"] = max(1, round(module["hours"] * ratio))
        
        # Recalculate to ensure exact total
        current_total = sum(module["hours"] for module in modules)
        if current_total != total_hours:
            diff = total_hours - current_total
            if diff > 0:
                # Add hours to largest module
                modules[-1]["hours"] += diff
            else:
                # Remove hours from smallest module
                modules[0]["hours"] = max(1, modules[0]["hours"] + diff)
        
        return modules
    
    def _create_study_plan(self, modules: list) -> list:
        """Create weekly study plan"""
        plan = []
        week = 1
        hours_per_week = 5  # Assume 5 hours per week
        
        current_module = 0
        while current_module < len(modules):
            week_plan = {
                "week": week,
                "modules": [],
                "hours": 0
            }
            
            week_hours = 0
            while current_module < len(modules) and week_hours + modules[current_module]["hours"] <= hours_per_week:
                module = modules[current_module]
                week_plan["modules"].append({
                    "title": module["title"],
                    "hours": module["hours"]
                })
                week_hours += module["hours"]
                current_module += 1
            
            # If module is too big, split it
            if current_module < len(modules) and week_hours < hours_per_week:
                remaining_hours = hours_per_week - week_hours
                if remaining_hours > 0:
                    module = modules[current_module]
                    week_plan["modules"].append({
                        "title": f"{module['title']} (Part 1)",
                        "hours": remaining_hours
                    })
                    modules[current_module]["hours"] -= remaining_hours
            
            week_plan["hours"] = week_hours
            plan.append(week_plan)
            week += 1
        
        return plan