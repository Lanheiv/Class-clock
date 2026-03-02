<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\DataRequest;

use Symfony\Component\Process\Process;
use Illuminate\Support\Facades\Storage;
use Symfony\Component\Process\Exception\ProcessFailedException;

class DataRequestController extends Controller
{
    public function request() {
        $error = null;
        $chack = $this->chack();

        if(!$chack) {
            $this->create();
        }

        $time = Storage::disk("local")->get("json/time.json");
        $jsonData = Storage::disk('local')->get('json/formatted_data.json');
        if(!$jsonData) {
            $jsonData = Storage::disk("local")->get('json/example.json');
            $error = ["Kļūda, nav iespējams iegūt jaunākos datus. Tiek izmantoti piemēra dati, kādas no funkcijām var nestrādāt dēļ tā."];
        }

        return response()->json(["data" => json_decode($jsonData, true), "time" => json_decode($time, true), "error" => $error]);
    }
    public function chack() {
        $existsToday = DataRequest::whereDate('created_at', now()->toDateString())->exists();

        if(!$existsToday) {
            return false;
        }
        return true;
    }
    public function create() {
        $process = new Process(['python', base_path('../scoper/main.py')], base_path('../'));
        $process->run();

        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        } else {
            DataRequest::create();
        }
    }
}