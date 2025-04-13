export class Schedule {
    constructor(mataKuliah, hari, waktu) {
      this.id = Date.now();
      this.mataKuliah = mataKuliah;
      this.hari = hari;
      this.waktu = waktu;
    }
  }
  