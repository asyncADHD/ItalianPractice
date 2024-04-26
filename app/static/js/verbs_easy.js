function allowDrop(event) {
    event.preventDefault();  // Allow dropping by preventing the default handling
}

function drag(event) {
    event.dataTransfer.setData("text", event.target.id);
    event.dataTransfer.effectAllowed = "move";
}

function drop(event) {
    event.preventDefault();
    const data = event.dataTransfer.getData("text");
    const draggedElement = document.getElementById(data);
    const dropTarget = event.target.closest('.drop-zone, .draggable-column');  // Accepts both drop zones and the draggable column

    // Ensure a valid drop target
    if (!dropTarget) return;

    // Allows dragging back to the draggable column
    if (dropTarget.classList.contains('draggable-column')) {
        dropTarget.appendChild(draggedElement);
    } else if (dropTarget.classList.contains('drop-zone')) {
        if (dropTarget.childNodes.length === 0 || dropTarget.firstChild === draggedElement) {
            dropTarget.appendChild(draggedElement);
        } else {
            // If the zone is already occupied, move the existing element back to the start area
            const existingChild = dropTarget.firstChild;
            document.querySelector('.draggable-column').appendChild(existingChild);
            dropTarget.appendChild(draggedElement);
        }
    }
}

function checkAnswers() {
    const zones = document.querySelectorAll('.drop-zone');
    let allCorrect = true;
    zones.forEach(zone => {
        if (zone.firstChild && zone.firstChild.id.replace('drag-', '') === zone.id) {
            zone.classList.add('correct');
            zone.classList.remove('incorrect');
        } else {
            zone.classList.add('incorrect');
            zone.classList.remove('correct');
            allCorrect = false;
        }
    });

    if (allCorrect) {
        document.getElementById('feedback-message').textContent = "All answers are correct! Choose an option below.";
        document.getElementById('feedback-popup').classList.add('show-popup');
        document.querySelector('.feedback-box').classList.add('show-popup');
    } else {
        document.getElementById('feedback-message').textContent = "Some answers are incorrect. Try again!";
        document.getElementById('feedback-popup').classList.add('show-popup');
        document.querySelector('.feedback-box').classList.add('show-popup');
    }
}

function resetPositions() {
    document.querySelectorAll('.drop-zone.incorrect').forEach(zone => {
        if (zone.firstChild) {
            document.querySelector('.draggable-column').appendChild(zone.firstChild);
        }
        zone.classList.remove('incorrect');
    });
    document.getElementById('feedback-popup').classList.remove('show-popup');
    document.querySelector('.feedback-box').classList.remove('show-popup');
}

function toggleTranslations() {
    const allDraggables = document.querySelectorAll('.draggable .content');
    allDraggables.forEach(content => {
        const italian = content.querySelector('.italian');
        const translation = content.querySelector('.translation');
        if (italian.style.display !== 'none') {
            italian.style.display = 'none';
            translation.style.display = 'block';  // Show translation
        } else {
            italian.style.display = 'block';
            translation.style.display = 'none';  // Hide translation
        }
    });
}

function resetAllPositions() {
    document.querySelectorAll('.drop-zone').forEach(zone => {
        if (zone.firstChild) {
            document.querySelector('.draggable-column').appendChild(zone.firstChild);
        }
        zone.classList.remove('incorrect', 'correct');
    });
    document.getElementById('feedback-popup').classList.remove('show-popup');
    document.querySelector('.feedback-box').classList.remove('show-popup');
}

document.getElementById('new-verb-button').addEventListener('click', function() {
    resetAllPositions();
    fetch('/verbs-easy')
        .then(response => response.text())
        .then(html => {
            document.getElementById('verb-container').innerHTML = html;
        })
        .catch(error => console.error('Error loading new verb:', error));
});
