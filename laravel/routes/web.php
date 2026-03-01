<?php

use Illuminate\Support\Facades\Route;

use App\Http\Controllers\IndexController;
use App\Http\Controllers\DataRequestController;

Route::get("/", [IndexController::class, "index"]);

Route::get("/lesson_data", [DataRequestController::class, "request"]);