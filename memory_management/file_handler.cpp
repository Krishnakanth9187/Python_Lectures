#include <iostream>
#include <fstream>
#include <string>

class FileHandler{
    public:
        FileHandler(const std::string filename){
            file.open(filename);
            if (!file.is_open()) {
            throw std::runtime_error("Cannot open file.");
            }
            std::cout << "File opened: " << filename << std::endl;
        }

        ~FileHandler(){
            if (file.is_open()) {
            file.close();
            std::cout << "File closed." << std::endl;
        }
    }

        void write(const std::string& data) {
        if (file.is_open()) {
            file << data << std::endl;
        }
        }

        

    private:
        std::ofstream file;
};

int main(){
    try{
        FileHandler fh("example.txt");
        fh.write("Hello, RAII!");
    }
    catch (const std::exception &e){
        std::cerr << e.what() << std::endl;
    }
    return 0;
}