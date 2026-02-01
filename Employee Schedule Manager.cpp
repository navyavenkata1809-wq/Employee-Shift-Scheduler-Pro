#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <random>
#include <ctime>
#include <iomanip>

using namespace std;

// Structure to hold employee details
struct Employee {
    string name;
    map<string, vector<string>> preferences; // Day -> List of shifts in priority order
    int daysWorked = 0;
    map<string, string> currentSchedule; // Day -> Assigned Shift
};

class ScheduleManager {
private:
    vector<string> days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
    vector<string> shifts = {"Morning", "Afternoon", "Evening"};
    vector<Employee> employees;
    map<string, map<string, vector<string>>> finalSchedule;

public:
    void addEmployee(string name) {
        Employee emp;
        emp.name = name;
    
        random_device rd;
        mt19937 g(rd());   // Random number generator
    
        for (const string& day : days) {
            vector<string> p = shifts;
    
            shuffle(p.begin(), p.end(), g);
    
            emp.preferences[day] = p;
            emp.currentSchedule[day] = "None";
        }
    
        employees.push_back(emp);
    }

    void assignShifts() {
        // First Pass: Assign based on priorities
        for (const string& day : days) {
            for (auto& emp : employees) {
                if (emp.daysWorked >= 5) continue;

                for (const string& preferredShift : emp.preferences[day]) {
                    // Check if shift has room (https://www.onlinegdb.com/#tab-stdinlimit to 3 for initial balance)
                    if (finalSchedule[day][preferredShift].size() < 3) {
                        finalSchedule[day][preferredShift].push_back(emp.name);
                        emp.daysWorked++;
                        emp.currentSchedule[day] = preferredShift;
                        break;
                    }
                }
            }
        }

        // Second Pass: Ensure minimum 2 employees per shift (Requirement 2.3)
        for (const string& day : days) {
            for (const string& shift : shifts) {
                while (finalSchedule[day][shift].size() < 2) {
                    bool assigned = false;
                    for (auto& emp : employees) {
                        if (emp.daysWorked < 5 && emp.currentSchedule[day] == "None") {
                            finalSchedule[day][shift].push_back(emp.name);
                            emp.daysWorked++;
                            emp.currentSchedule[day] = shift;
                            assigned = true;
                            break;
                        }
                    }
                    if (!assigned) break; // No more eligible employees
                }
            }
        }
    }

    void display() {
        cout << setfill('=') << setw(50) << "" << endl;
        cout << "         COMPANY WEEKLY SHIFT SCHEDULE" << endl;
        cout << setfill('=') << setw(50) << "" << setfill(' ') << endl;

        for (const string& day : days) {
            cout << "\n>>> " << day << " <<<" << endl;
            for (const string& shift : shifts) {
                cout << left << setw(12) << shift << ": ";
                vector<string> workers = finalSchedule[day][shift];
                if (workers.empty()) {
                    cout << "NO STAFF ASSIGNED";
                } else {
                    for (size_t i = 0; i < workers.size(); ++i) {
                        cout << workers[i] << (i == workers.size() - 1 ? "" : ", ");
                    }
                }
                cout << endl;
            }
        }
        cout << "\n" << setfill('=') << setw(50) << "" << endl;
    }
};

int main() {
    ScheduleManager manager;
    
    // Input/Storage (Requirement 2.1)
    vector<string> staff = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"};
    for (const string& name : staff) {
        manager.addEmployee(name);
    }

    manager.assignShifts();
    manager.display();

    return 0;
}
