<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\DataRequest;

use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

class DataRequestController extends Controller
{
    public function DataChack() {
        $existsToday = DataRequest::whereDate('created_at', now()->toDateString())->exists();

        if(!$existsToday) {
            return false;
        }
        return true;
    }
    public function DataCreate() {
        $process = new Process(['python', base_path('../scoper/main.py')], base_path('../'));
        $process->run();

        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        } else {
            DataRequest::create(["status" => "success"]);
        }
    }
}