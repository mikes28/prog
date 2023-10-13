#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <numeric>
#include <map>

struct hills
{
    std::string hegyseg;
    std::string csucs;
    int magassag;
    double magassag_in_feet;
};
std::map<std::string, int> Counts = {};

void input(std::ifstream &input_file, std::vector<hills> &hegyek, hills &max_value, double &sum , double &max_value_borzsony, int &higher3000){
if (!input_file.is_open())
    {
        std::cout << "A file megnyitása meghiúsult" << std::endl;
    }
    std::string line;
    std::getline(input_file, line);
    while (std::getline(input_file, line))
    {
        std::istringstream iss(line);
        hills data;
        std::string token;
        std::cout << line << std::endl;
        while (std::getline(iss, token, ';'))
        {
           if (data.csucs.empty())
            {
                data.csucs=token;
            }
            else if (data.hegyseg.empty())
            {
                data.hegyseg=token;
            }else{
                data.magassag=std::stoi(token);
                data.magassag_in_feet=std::stod(token)*3.280839895;
            }          
        }
        if (data.magassag_in_feet>3000.0)
        {
            std::cout<<data.magassag_in_feet;
        }
        
        
        sum+=data.magassag; /* ossz magassag kiszamolasa az atlagszamitashoz */
        if (data.magassag>max_value.magassag)
        {
            max_value=data;
        }
        if (data.hegyseg=="Börzsöny"&&data.magassag>max_value_borzsony)
        {
            max_value_borzsony+=data.magassag;
        }
      
        auto contain =Counts.find(data.hegyseg);
        if (contain != Counts.end())
        {
            contain->second++;
        }else{
            Counts.emplace(data.hegyseg, 0);
        }
        hegyek.push_back(data);
    }
}

void check(const std::vector<hills> &hegyek){
     for (const hills &d : hegyek)

        {   
            std::cout<<"lefit";
            std::cout << "Hegység : " << d.hegyseg;
            std::cout << "Csúcs:  " << d.csucs;
            std::cout << "Magasság:  " << d.magassag << std::endl;
        }
}

int main()
{
    int higher3000;   
    double sum, max_value_borzsony;
    hills max_value={"", "", 0};
    std::ifstream input_file;
    input_file.open("inputs/hegyekMo.txt");
    std::vector<hills> hegyek;
    input(input_file, hegyek, max_value, sum, max_value_borzsony, higher3000);
    check(hegyek);

    std::cout<<"Megadott hegységek száma: "<<hegyek.size()<<std::endl;

    sum=sum/hegyek.size();
    std::cout<<"A hegyek átlagmagassága: "<<sum<<std::endl;


    std::cout<<std::endl<<"A legmagasabb  ";
    std::cout << "Hegység : " << max_value.hegyseg << std::endl;
    std::cout << "Csúcs:  " << max_value.csucs << std::endl;
    std::cout << "Magasság:  " << max_value.magassag << std::endl;

 


 
    std::cout<<"Kérlek adj meg egy magasságot"<<std::endl;
    int inp;
    std::cin>>inp;
    (max_value_borzsony>inp)?std::cout<<"Van ":std::cout<<"Nincs ";
    std::cout<<inp<<" méternél magasabb hegycsúcs a Börzsönyben"<<std::endl;

    for (auto &item : Counts)
    {
        std::cout<<item.first<<" : "<<item.second<<std::endl;
    }
    std::cout<<"3000 lábnál magasabb hegységek száma ";
    
    
}
