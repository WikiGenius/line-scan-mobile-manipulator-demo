cmake_minimum_required(VERSION 3.8)
project(line_scan_mobile_manipulator_demo)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  launch
  docs
  experiments
  results
  media
  src
  DESTINATION share/${PROJECT_NAME}
  OPTIONAL
)

ament_package()
