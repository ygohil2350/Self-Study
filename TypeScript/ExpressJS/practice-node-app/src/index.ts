import express, { Request, Response } from "express";

const app = express();

interface ListData {
  id: string;
  name: string;
  phone: number;
}

app.listen(8080, () => {
  console.log("Server is running on port 8080");
});

let list: ListData[] = [];

app.get("/", (_: Request, res: Response) => {
  res.status(204).json(list);
});

app.post("/", (request, response) => {
  if (request.body.name && request.body.phone) {
    const { name, phone } = request.body;
    list.push({ name, phone, id: crypto.randomUUID() });
    response.status(204).json(list);
  } else {
    response.status(500).json({ message: "Missing mandatory Data" });
  }
});

app.put("/:id", (request, response) => {
  if (request.body.name && request.body.phone && request.params.id) {
    const { name, phone } = request.body;
    list = list.map((ele) =>
      ele.id === request.params.id ? { ...ele, name, phone } : ele
    );
    response.status(204).json(list);
  } else {
    response.status(500).json({ message: "Missing mandatory Data" });
  }
});
