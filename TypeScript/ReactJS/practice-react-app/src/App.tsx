import { DataGrid, GridRowsProp, GridColDef } from "@mui/x-data-grid";
import "./App.css";
import {
  Box,
  Button,
  Dialog,
  Snackbar,
  SnackbarCloseReason,
  TextField,
} from "@mui/material";
import { useState } from "react";

function App() {
  const initialColumnData = {
    field: "",
    headerName: "",
    width: "",
  };
  const [rows, setRows] = useState([]);
  const [columns, setColumns] = useState<GridColDef[]>([]);
  const [openSnackbar, setOpenSnackbar] = useState({
    state: false,
    message: "",
  });
  const [openAddCol, setOpenAddCol] = useState(false);
  const [addColData, setAddColData] = useState(initialColumnData);
  const [openAddRow, setOpenAddRow] = useState(false);
  // const rows: GridRowsProp = [
  //   { id: 1, col1: "Hello", col2: "World" },
  //   { id: 2, col1: "DataGridPro", col2: "is Awesome" },
  //   { id: 3, col1: "MUI", col2: "is Amazing" },
  // ];

  // const columns: GridColDef[] = [
  //   { field: "col1", headerName: "Column 1", width: 150 },
  //   { field: "col2", headerName: "Column 2", width: 150 },
  // ];
  const handleAddColumn = () => {
    setOpenAddCol(true);
  };
  const handleSubmitColData = (event: any) => {
    event.preventDefault();
    setColumns((pre) => [
      ...pre,
      {
        field: addColData.field,
        headerName: addColData.headerName,
        width: Number(addColData.width),
      },
    ]);
    handleCancelColData();
  };
  const handleCancelColData = () => {
    setAddColData(initialColumnData);
    setOpenAddCol(false);
  };
  const handleColDataChange = (e: any) => {
    setAddColData((pre) => ({ ...pre, [e.target.name]: e.target.value }));
  };
  const handleAddRow = () => {
    if (columns.length === 0) {
      setOpenSnackbar({ state: true, message: "Please add a column first" });
      return;
    }
    setOpenAddRow(true);
  };
  const handleCloseSnackbar = () => {
    setOpenSnackbar({ state: false, message: "" });
  };
  return (
    <div style={{ height: 300, width: "100%" }}>
      <Box sx={{ display: "flex", justifyContent: "end" }}>
        <Button onClick={handleAddColumn}>Add Column</Button>
        <Button onClick={handleAddRow}>Add Row</Button>
      </Box>
      <DataGrid rows={rows} columns={columns} />
      <Dialog open={openAddCol}>
        <Box sx={{ pl: 3 }}>
          <h3>Add Column</h3>
        </Box>
        <Box component="form" onSubmit={handleSubmitColData}>
          <Box sx={{ "& > :not(style)": { m: 1, width: "30%" }, mr: 1, ml: 1 }}>
            <TextField
              fullWidth
              defaultValue={addColData.headerName}
              label="Header Name"
              variant="standard"
              name="headerName"
              onChange={handleColDataChange}
              required
            />
            <TextField
              fullWidth
              label="Field Key"
              defaultValue={addColData.field}
              variant="standard"
              name="field"
              onChange={handleColDataChange}
              required
            />
            <TextField
              fullWidth
              label="width"
              defaultValue={addColData.width}
              name="width"
              type="number"
              variant="standard"
              onChange={handleColDataChange}
              required
            />
          </Box>
          <Box
            sx={{
              display: "flex",
              justifyContent: "end",
              m: 2,
            }}
          >
            <Button onClick={handleCancelColData}>Cancel</Button>
            <Button type="submit">Save</Button>
          </Box>
        </Box>
      </Dialog>
      <Dialog open={openAddRow}>
        <Box sx={{ pl: 3 }}>
          <h3>Add Column</h3>
        </Box>
        <Box component="form" onSubmit={handleSubmitRowData}>
          <Box sx={{ "& > :not(style)": { m: 1, width: "30%" }, mr: 1, ml: 1 }}>
            <TextField
              fullWidth
              defaultValue={addColData.headerName}
              label="Header Name"
              variant="standard"
              name="headerName"
              onChange={handleRowDataChange}
              required
            />
          </Box>
          <Box
            sx={{
              display: "flex",
              justifyContent: "end",
              m: 2,
            }}
          >
            <Button onClick={handleCancelColData}>Cancel</Button>
            <Button type="submit">Save</Button>
          </Box>
        </Box>
      </Dialog>
      <Snackbar
        open={openSnackbar.state}
        autoHideDuration={3000}
        onClose={handleCloseSnackbar}
        message={openSnackbar.message}
      />
    </div>
  );
}

export default App;
