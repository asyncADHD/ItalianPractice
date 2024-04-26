// Prevents the default behavior to enable dropping of elements
function allowDrop(event) {
    event.preventDefault();
}

// Sets the data type and id of the dragged element
function drag(event) {
    event.dataTransfer.setData("text", event.target.id);
    event.dataTransfer.effectAllowed = "move";
}

// Handles the drop action for elements
function drop(event) {
    event.preventDefault();
    const data = event.dataTransfer.getData("text");
    const draggedElement = document.getElementById(data);
    const dropTarget = event.target.closest('.drop-zone, .draggable-column');

    if (!dropTarget) return;  // Stops the function if no valid drop target is found

    if (dropTarget.classList.contains('draggable-column')) {
        dropTarget.appendChild(draggedElement);
    } else if (dropTarget.classList.contains('drop-zone')) {
        handleDropZoneOccupancy(dropTarget, draggedElement);
    }
}

// Manages the drop zone occupancy
function handleDropZoneOccupancy(dropTarget, draggedElement) {
    if (dropTarget.childNodes.length === 0 || dropTarget.firstChild === draggedElement) {
        dropTarget.appendChild(draggedElement);
    } else {
        const existingChild = dropTarget.firstChild;
        document.querySelector('.draggable-column').appendChild(existingChild);
        dropTarget.appendChild(draggedElement);
    }
}

// Checks if all answers placed in drop zones are correct
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

    updateFeedback(allCorrect);
}

// Updates the feedback message based on whether all answers are correct
function updateFeedback(allCorrect) {
    const message = allCorrect ? "All answers are correct! Choose an option below." : "Some answers are incorrect. Try again!";
    document.getElementById('feedback-message').textContent = message;
    document.getElementById('feedback-popup').classList.add('show-popup');
    document.querySelector('.feedback-box').classList.add('show-popup');
}

// Resets the positions of elements in incorrect drop zones
function resetPositions() {
    document.querySelectorAll('.drop-zone.incorrect').forEach(zone => {
        if (zone.firstChild) {
            document.querySelector('.draggable-column').appendChild(zone.firstChild);
        }
        zone.classList.remove('incorrect');
    });
    closeFeedbackPopup();
}

// Closes the feedback popup
function closeFeedbackPopup() {
    document.getElementById('feedback-popup').classList.remove('show-popup');
    document.querySelector('.feedback-box').classList.remove('show-popup');
}

// Toggles the display of translations for each draggable
function toggleTranslations() {
    document.querySelectorAll('.draggable .content').forEach(content => {
        const italian = content.querySelector('.italian');
        const translation = content.querySelector('.translation');
        italian.style.display = (italian.style.display !== 'none') ? 'none' : 'block';
        translation.style.display = (translation.style.display !== 'none') ? 'none' : 'block';
    });
}

// Resets the positions of all draggables
function resetAllPositions() {
    document.querySelectorAll('.drop-zone').forEach(zone => {
        if (zone.firstChild) {
            document.querySelector('.draggable-column').appendChild(zone.firstChild);
        }
        zone.classList.remove('incorrect', 'correct');
    });
}

// Initializes event listeners on document load
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('new-verb-button').addEventListener('click', function() {
        resetAllPositions();  // Resets all positions to default
        fetchNewVerb();  // Fetches new verbs from the server
    });
});

// Fetches new verb conjugations from the server
function fetchNewVerb() {
    console.log("Fetching new verbs");
    fetch('/get-verbs-easy')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log("Received data:", data);
            updateDraggableArea(data);  // Update to call a function to handle draggable area updates
        })
        .catch(error => console.error('Error loading new verb:', error));
    closeFeedbackPopup();
}

// Updates the draggable area with new elements
function updateDraggableArea(data) {
    const draggableArea = document.querySelector('.draggable-column'); // Ensure this is the correct class for the draggable container
    if (!draggableArea) {
        console.log("No draggable area found, please check your HTML structure.");
        return;
    }

    // Clear the current contents
    while (draggableArea.firstChild) {
        draggableArea.removeChild(draggableArea.firstChild);
    }

    // Add new draggable items
    Object.keys(data).forEach(key => {
        console.log("Adding new data for key:", key);
        draggableArea.appendChild(createDraggableElement(key, data[key]));
    });
}

// Creates a draggable element with Italian and English content
function createDraggableElement(key, content) {
    const draggableDiv = document.createElement('div');
    draggableDiv.className = 'draggable';
    draggableDiv.id = `drag-${key}`;
    draggableDiv.setAttribute('draggable', 'true');
    draggableDiv.ondragstart = drag;  // Make sure you have a 'drag' function defined that sets up the drag events

    const contentDiv = document.createElement('div');
    contentDiv.className = 'content';

    const italianSpan = document.createElement('span');
    italianSpan.className = 'italian';
    italianSpan.textContent = content['Italian'];

    const englishSpan = document.createElement('span');
    englishSpan.className = 'translation';
    englishSpan.textContent = content['English'];
    englishSpan.style.display = 'none'; // Hidden by default, can be toggled

    contentDiv.appendChild(italianSpan);
    contentDiv.appendChild(englishSpan);
    draggableDiv.appendChild(contentDiv);

    return draggableDiv;
}