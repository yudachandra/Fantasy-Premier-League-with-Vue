<template>
  <div class="fpl-page">
    <h1 class="page-title">FPL Data</h1>
    <table class="data-table">
      <thead>
        <tr>
          <th @click="sortByColumn('name')">Name</th>
          <th @click="sortByColumn('position')">Position</th>
          <th @click="sortByColumn('team')">Team</th>
          <th @click="sortByColumn('expected_assists')">xA</th>
          <th @click="sortByColumn('expected_goal_involvements')">xGi</th>
          <th @click="sortByColumn('expected_goals')">xG</th>
          <th @click="sortByColumn('expected_goals_conceded')">xGc</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in sortedData" :key="`row_${index}`" @click="toggleRowDetails(row)">
          <td>{{ row.name }}</td>
          <td>{{ row.position }}</td>
          <td>{{ row.team }}</td>
          <td>{{ row.expected_assists }}</td>
          <td>{{ row.expected_goal_involvements }}</td>
          <td>{{ row.expected_goals }}</td>
          <td>{{ row.expected_goals_conceded }}</td>
        </tr>
        <!-- Add a row for showing details -->
        <tr v-if="expandedRow" class="details-row">
          <td colspan="7">
            <div class="details-container" :class="{ 'fade-in': expandedRow }">
              <!-- Add details here -->
              <p class="details-title">Details:</p>
              <p class="details-info">Name: {{ expandedRow.name }}</p>
              <!-- Add more details as needed -->
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import Papa from 'papaparse';

export default {
  data() {
    return {
      data: [],
      sortedData: [],
      sortKey: null,
      sortDirection: 1,
      expandedRow: null,
    };
  },
  mounted() {
    fetch('/data/2023-24/gws/merged_gw.csv')
      .then((response) => response.text())
      .then((csv) => {
        this.data = this.parseCSV(csv);
        this.sortedData = this.data;
      });
  },
  methods: {
    parseCSV(csv) {
      const parsed = Papa.parse(csv, {
        header: true,
        skipEmptyLines: true,
      });

      return parsed.data;
    },

    sortByColumn(key) {
      if (this.sortKey === key) {
        this.sortDirection *= -1;
      } else {
        this.sortKey = key;
        this.sortDirection = 1;
      }

      this.sortedData = this.data.slice().sort((a, b) => {
        const aVal = a[key];
        const bVal = b[key];
        return aVal < bVal ? -1 * this.sortDirection : 1 * this.sortDirection;
      });
    },
    toggleRowDetails(row) {
      if (this.expandedRow === row) {
        this.expandedRow = null;
      } else {
        this.expandedRow = row;
      }
    },
  },
};
</script>

<style scoped>
.fpl-page {
  font-family: Arial, sans-serif;
  padding: 20px;
  background-color: #f7f7f7;
}

.page-title {
  font-size: 24px;
  margin-bottom: 20px;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.data-table th {
  background-color: #0078d4;
  color: #fff;
  cursor: pointer;
}

.data-table th,
.data-table td {
  padding: 12px;
  text-align: left;
  border: 1px solid #d3d3d3;
}

.data-table tr:nth-child(even) {
  background-color: #f2f2f2;
}

.details-row {
  background-color: #f2f2f2;
}

.details-container {
  padding: 10px;
  animation: fadeIn 0.5s;
  opacity: 0;
  transition: opacity 0.5s ease-in-out;
}

.details-title {
  font-weight: bold;
  font-size: 18px;
}

.details-info {
  font-size: 16px;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.fade-in {
  opacity: 1 !important;
}
</style>
