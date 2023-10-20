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


int input(std::ifstream &input_file, std::vector<hills> &hegyek, hills &max_value, double &sum , double &max_value_borzsony, int &higher3000, std::map<std::string, int> &Counts){
if (!input_file.is_open())
    {
        std::cout << "A file megnyitása meghiúsult" << "\n";
        return -1;
    }
    std::string line;
    std::getline(input_file, line);
    while (std::getline(input_file, line))
    {
        std::istringstream iss(line);
        hills data;
        std::string token;
        std::cout << line << "\n";


    for (int i = 0; std::getline(iss, token, ';'); ++i)
    {
        if (i==0)
        {
            data.csucs=std::move(token);
        }
        else if (i==1)
        {
            data.hegyseg=std::move(token);
        }
        else{
         data.magassag=std::stoi(token);
         data.magassag_in_feet=data.magassag*3.280839895;
        }
    }

        if (data.magassag_in_feet > 3000.0) {
            higher3000++;
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
        hegyek.push_back(std::move(data));
    }
        return 0;
}

void check(const std::vector<hills> &hegyek){
     for (const hills &d : hegyek)
        {   
            std::cout<<"lefit";
            std::cout << "Hegység : " << d.hegyseg;
            std::cout << "Csúcs:  " << d.csucs;
            std::cout << "Magasság:  " << d.magassag <<"\n";
        }
}

void outData(std::ofstream &output_file, std::vector<hills> &hegyek){

    output_file<<"Hegycsúcs neve; Magasság láb"<<"\n";
    for (auto &d : hegyek)
    {
        output_file<<d.csucs<<';'<<d.magassag_in_feet<<"\n";
    }
    

}

int main()
{

    std::map<std::string, int> Counts = {};
    int higher3000 =0;   
    double sum, max_value_borzsony;
    hills max_value={"", "", 0};
    std::ifstream input_file;
    std::ofstream output_file;
    input_file.open("inputs/hegyekMo.txt");
    output_file.open("output.txt");
    std::vector<hills> hegyek;
   if ( input(input_file, hegyek, max_value, sum, max_value_borzsony, higher3000, Counts)!=0)
   {
    return 1;
   }
   
    check(hegyek);
    outData(output_file, hegyek);
    std::cout<<"Megadott hegységek száma: "<<hegyek.size()<<"\n";

    sum=sum/hegyek.size();
    std::cout<<"A hegyek átlagmagassága: "<<sum<<"\n";


    std::cout<<"\n"<<"A legmagasabb  ";
    std::cout << "Hegység : " << max_value.hegyseg << "\n";
    std::cout << "Csúcs:  " << max_value.csucs << "\n";
    std::cout << "Magasság:  " << max_value.magassag << "\n";

 


 
    std::cout<<"Kérlek adj meg egy magasságot"<<"\n";
    int inp;
    std::cin>>inp;
    (max_value_borzsony>inp)?std::cout<<"Van ":std::cout<<"Nincs ";
    std::cout<<inp<<" méternél magasabb hegycsúcs a Börzsönyben"<<"\n";

    for (auto &item : Counts)
    {
        std::cout<<item.first<<" : "<<item.second<<"\n";
    }
    std::cout<<"3000 lábnál magasabb hegységek száma "<<higher3000<<"\n";
    
    
}
