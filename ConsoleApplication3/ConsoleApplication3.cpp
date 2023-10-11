#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <jpeglib.h>
#include <png.h>
#include <boost/filesystem.hpp>

namespace fs = boost::filesystem;

void convertJpegToPng(const char* jpegFile, const char* pngFile) {
    // ... (same as previous code)
}

int main() {
    const char* inputFolder = "input_folder";
    const char* outputFolder = "output_folder";

    // Create output folder if it doesn't exist
    fs::create_directories(outputFolder);

    for (const auto& entry : fs::directory_iterator(inputFolder)) {
        if (entry.is_regular_file() && entry.path().extension() == ".jpg") {
            const std::string inputJpegFile = entry.path().string();
            const std::string outputPngFile = fs::path(outputFolder) / entry.path().stem().string() + ".png";
            convertJpegToPng(inputJpegFile.c_str(), outputPngFile.c_str());
            std::cout << "Converted: " << inputJpegFile << " -> " << outputPngFile << std::endl;
        }
    }

    return 0;
}
