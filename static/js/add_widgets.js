const addwidgethtml = `
<div id="widgetModal" class="modal">
    <div class="modal-content">
        <div class="modal-header">
            <h2 class="modal-title">Edit widgets</h2>
            <button class="close-btn" onclick="closeModal()">&times;</button>
        </div>

        <div class="community-details-widget">
            <i class="bi bi-pin-angle"></i>
            <div class="community-details-text">
                <strong>Community details</strong>
                <p>Describe your community and members. Always at the top of your widgets.</p>
            </div>
            <p> > </p>
        </div>

        <div class="add-widget">
            <select name="addwidget">
                <option value="postflair">postflair</option>
                <option value="rules">rules</option>
            </select>
        </div>

        <div class="modal-footer">
            <button class="btn btn-cancel" onclick="closeModal()">Cancel</button>
            <button class="btn btn-save" onclick="saveAndRedirect()">Save</button>
        </div>
    </div>
</div>
`

const editWidgetBtn = document.getElementById('edit-widget-button');


function openModal() {
    const container = document.getElementById('modal-container')
    const modalElement = document.createElement('div');
    modalElement.innerHTML = addwidgethtml;
    container.appendChild(modalElement);

    const modal = document.getElementById('widgetModal');
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    const modal = document.getElementById('widgetModal');
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

editWidgetBtn.addEventListener('click', openModal);

function saveAndRedirect() {
    const selectElement = document.querySelector('select[name="addwidget"]');
    const optionValue = selectElement.value;
    const communityName = document.getElementById('modal-container').dataset.communityName

    if (optionValue) {
        window.location.href = `http://localhost:8000/d/mod/${communityName}/${optionValue}`;
    }
}