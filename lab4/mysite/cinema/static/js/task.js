// Инициализируем стартовый набор учеников
var initialStudents = [
  { firstName: "Злата", lastName: "Медведева", physicsGrade: 1, mathGrade: 2, literatureGrade: 3 },
  { firstName: "Диана", lastName: "Фетисова", physicsGrade: 5, mathGrade: 5, literatureGrade: 4 },
  { firstName: "Вероника", lastName: "Ушакова", physicsGrade: 3, mathGrade: 3, literatureGrade: 4 },
  { firstName: "Егор", lastName: "Ситников", physicsGrade: 4, mathGrade: 4, literatureGrade: 4 },
  { firstName: "Анатолий", lastName: "Губанов", physicsGrade: 2, mathGrade: 2, literatureGrade: 4 }
];

// Добавляем начальных учеников в список
for (var i = 0; i < initialStudents.length; i++) {
  var student = initialStudents[i];
  addStudentToList(student);
  if (student.physicsGrade >= 4 && student.mathGrade >= 4 && student.literatureGrade >= 4) {
    addStudentToResults(student);
  }
}


// Слушаем событие отправки формы для добавления ученика
document.getElementById('addStudentForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Предотвращаем обновление страницы
  var form = event.target;

  // Получаем значения полей формы
  var firstName = form.elements.firstName.value;
  var lastName = form.elements.lastName.value;
  var physicsGrade = parseInt(form.elements.physicsGrade.value);
  var mathGrade = parseInt(form.elements.mathGrade.value);
  var literatureGrade = parseInt(form.elements.literatureGrade.value);

  // Создаем объект с информацией об ученике
  var student = {
    firstName: firstName,
    lastName: lastName,
    physicsGrade: physicsGrade,
    mathGrade: mathGrade,
    literatureGrade: literatureGrade
  };

  // Добавляем ученика в список учеников
  addStudentToList(student);

  // Проверяем, удовлетворяет ли ученик условию задачи
  if (student.physicsGrade >= 4 && student.mathGrade >= 4 && student.literatureGrade >= 4) {
    // Ученик удовлетворяет условию задачи, добавляем его в список результатов
    addStudentToResults(student);
  }

  // Очищаем значения полей формы
  form.reset();
});

// Функция для добавления ученика в список учеников
function addStudentToList(student) {
  var studentsTable = document.getElementById('studentsTable');
  var newRow = studentsTable.insertRow();

  var firstNameCell = newRow.insertCell();
  firstNameCell.textContent = student.firstName;

  var lastNameCell = newRow.insertCell();
  lastNameCell.textContent = student.lastName;

  var physicsGradeCell = newRow.insertCell();
  physicsGradeCell.textContent = student.physicsGrade;

  var mathGradeCell = newRow.insertCell();
  mathGradeCell.textContent = student.mathGrade;

  var literatureGradeCell = newRow.insertCell();
  literatureGradeCell.textContent = student.literatureGrade;
}

// Функция для добавления ученика в список результатов
function addStudentToResults(student) {
  var resultsList = document.getElementById('resultsList');
  var listItem = document.createElement('li');
  listItem.textContent = student.firstName + ' ' + student.lastName;
  listItem.classList.add('success');
  resultsList.appendChild(listItem);
}
