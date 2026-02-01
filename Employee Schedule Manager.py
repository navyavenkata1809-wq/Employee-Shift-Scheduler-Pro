import random

class Employee:
    """Represents an employee with preferences and tracking for shifts worked."""
    def __init__(self, name):
        self.name = name
        # Preferences: {Day: [Priority 1, Priority 2, Priority 3]}
        self.preferences = {}
        self.days_worked = 0
        self.schedule = {day: None for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

    def add_preference(self, day, pref_list):
        self.preferences[day] = pref_list

class ScheduleManager:
    """Manages the logic for assigning shifts based on company rules."""
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.shifts = ["Morning", "Afternoon", "Evening"]
        self.employees = []
        # Final schedule structure: {Day: {Shift: [Employee Names]}}
        self.final_schedule = {day: {shift: [] for shift in self.shifts} for day in self.days}

    def add_employee(self, employee):
        self.employees.append(employee)

    def resolve_and_assign(self):
        """Main logic to assign shifts while respecting constraints."""
        
        # Step 1: Attempt to assign based on preferences
        for day in self.days:
            for emp in self.employees:
                if emp.days_worked >= 5:
                    continue
                
                # Check preferences in priority order (Bonus Feature)
                prefs = emp.preferences.get(day, [])
                assigned = False
                
                for preferred_shift in prefs:
                    # Logic: Try to assign if the preferred shift isn't overly crowded yet
                    # We'll fill preferred slots first
                    if len(self.final_schedule[day][preferred_shift]) < 5: # Soft cap for initial pass
                        self.final_schedule[day][preferred_shift].append(emp.name)
                        emp.days_worked += 1
                        emp.schedule[day] = preferred_shift
                        assigned = True
                        break
                
                # If no preference could be met, we will handle them in the "fill requirements" phase

        # Step 2: Ensure minimum 2 employees per shift (Requirement 2.3)
        for day in self.days:
            for shift in self.shifts:
                while len(self.final_schedule[day][shift]) < 2:
                    # Find employees who haven't worked 5 days and aren't working today
                    available = [e for e in self.employees 
                                if e.days_worked < 5 and e.schedule[day] is None]
                    
                    if not available:
                        break # No more available employees to fill the gap
                    
                    chosen = random.choice(available)
                    self.final_schedule[day][shift].append(chosen.name)
                    chosen.days_worked += 1
                    chosen.schedule[day] = shift

    def display_schedule(self):
        """Prints the final schedule in a readable format."""
        print("="*60)
        print(f"{'WEEKLY EMPLOYEE SCHEDULE':^60}")
        print("="*60)
        for day in self.days:
            print(f"\n[ {day.upper()} ]")
            for shift in self.shifts:
                workers = ", ".join(self.final_schedule[day][shift]) if self.final_schedule[day][shift] else "No staff assigned"
                print(f"  {shift:10}: {workers}")
        print("\n" + "="*60)

def main():
    manager = ScheduleManager()
    
    # Mock data collection (Requirement 2.1)
    # In a real app, this could be input() calls in a loop
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"]
    
    for name in names:
        emp = Employee(name)
        # Randomly assign priorities for demonstration
        for day in manager.days:
            prefs = random.sample(manager.shifts, 3) # Random priority: [1st, 2nd, 3rd]
            emp.add_preference(day, prefs)
        manager.add_employee(emp)

    # Run logic
    manager.resolve_and_assign()
    
    # Output (Requirement 2.4)
    manager.display_schedule()

if __name__ == "__main__":
    main()