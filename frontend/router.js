
import express from "express";
import { home,code }  from "./controller";

const router =express.Router()


router.get("/:code",code);
router.get("/", home);

// router.get("/getItems", getItems);


export default router;