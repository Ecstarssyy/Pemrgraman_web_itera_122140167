import { Schedule } from './schedule.js';

const getSchedules = () => JSON.parse(localStorage.getItem('jadwalKuliah')) || [];

const saveSchedules = (schedules) => localStorage.setItem('jadwalKuliah', JSON.stringify(schedules));

const renderSchedules = () => {
  const schedules = getSchedules();
  const list = document.getElementById('scheduleList');
  list.innerHTML = schedules.map(schedule => `
    <div class="schedule-item">
      <strong>${schedule.mataKuliah}</strong><br/>
      ${schedule.hari} - ${schedule.waktu}
      <div class="actions">
        <button onclick="editSchedule(${schedule.id})">Edit</button>
        <button onclick="deleteSchedule(${schedule.id})">Hapus</button>
      </div>
    </div>
  `).join('');
};

// Dibuat global supaya bisa dipanggil dari HTML
window.editSchedule = (id) => {
  const schedules = getSchedules();
  const schedule = schedules.find(s => s.id === id);
  document.getElementById('mataKuliah').value = schedule.mataKuliah;
  document.getElementById('hari').value = schedule.hari;
  document.getElementById('waktu').value = schedule.waktu;
  deleteSchedule(id);
};

window.deleteSchedule = (id) => {
  const schedules = getSchedules().filter(s => s.id !== id);
  saveSchedules(schedules);
  renderSchedules();
};

document.getElementById('scheduleForm').addEventListener('submit', async (event) => {
  event.preventDefault();
  const mataKuliah = document.getElementById('mataKuliah').value;
  const hari = document.getElementById('hari').value;
  const waktu = document.getElementById('waktu').value;
  const newSchedule = new Schedule(mataKuliah, hari, waktu);
  const schedules = getSchedules();
  schedules.push(newSchedule);
  saveSchedules(schedules);
  renderSchedules();
  event.target.reset();
});

window.onload = () => renderSchedules();
