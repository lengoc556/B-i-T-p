var student = {
    name :'ngoc',
    age: 18,
    grade:'B', 
    isEnrolled:true ,
}
console.log(student)
student.address = "123 Main St";


student.grade = "A+";


delete student.isEnrolled;

console.log("Student sau khi cập nhật:", student);
