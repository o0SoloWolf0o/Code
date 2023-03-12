function addTask() {
    const deleteButton = document.createElement('button');
    const deleteIcon = document.createElement('i');
    deleteIcon.classList.add('fa', 'fa-trash');
    deleteButton.appendChild(deleteIcon);
    deleteButton.addEventListener('click', removeTask);

    const taskText = document.querySelector('.add-box').value;
    if (!taskText) {
        // if the task text is empty, don't add a new task
        return;
    }

    const taskList = document.querySelector('#task-list');
    const li = document.createElement('li');
    li.classList.add('task');
    li.innerHTML = taskText;
    li.insertBefore(deleteButton, li.childNodes[0]);
    taskList.appendChild(li);

    document.querySelector('.add-box').value = '';
}




var plus = document.querySelector('#plus');
plus.addEventListener('click', addTask);

document.querySelector('.add-box').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        addTask();
    }
});

function removeTask(event) {
    const task = event.target.closest('.task');
    if (task) {
        if (task.classList.contains('done')) {
            // if the task is already marked as done, remove it
            task.remove();
        } else {
            // otherwise, mark it as done
            task.classList.add('done');
        }
    }
}


var trashIcons = document.getElementsByClassName('fa-trash');

for (var i = 0; i < trashIcons.length; i++) {
    trashIcons[i].addEventListener('click', removeTask);
}