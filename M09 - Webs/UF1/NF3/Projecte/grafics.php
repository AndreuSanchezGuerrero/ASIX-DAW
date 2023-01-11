<?php
    // Require the necessary JpGraph files
    require_once 'jpgraph/src/jpgraph.php';
    require_once 'jpgraph/src/jpgraph_line.php';
    require_once 'jpgraph/src/jpgraph_bar.php';

    // Connect to the database
    $conn = connectar();
    
    // Get the data from the database
    //We select the last 24 hours
    $sql = "SELECT * FROM meteo WHERE id > (SELECT MAX(id) - 24 FROM meteo) ORDER BY id ASC";
    $result = $conn->query($sql);
    if ($result->rowCount() > 0) {
        while($row = $result->fetch()) {
            $datax[] = $row["hour"];
            $tempx[] = $row["temp"];
            $humx[] = $row["humidity"];
            $precipx[] = $row["precip"];
            $velx[] = $row["windspeed"];
            $dirx[] = $row["winddir"];
        }
    } else {
        echo "0 results";
    }
    tancar($conn);
    //Temperature
    $graph = new Graph(600,400);
    $graph->SetScale("textlin");
    $graph->img->SetMargin(40,40,40,40);
    $graph->SetShadow();
    $graph->title->Set("Temperatura");
    $graph->xaxis->title->Set("Temps");
    $graph->yaxis->title->Set("Temperatura");
    $graph->xaxis->SetTickLabels($datax);
    $bplot = new BarPlot($tempx);
    $bplot->SetFillColor("blue");
    $bplot->SetShadow();
    $avg = array_sum($tempx)/count($tempx);
    $avg = array_fill(0, count($tempx), $avg);
    $lineplot=new LinePlot($avg);
    $lineplot->SetColor("red");
    $graph->Add($bplot);
    $graph->Add($lineplot);
    $graph->Stroke("imatges/grafics/temperatura.png");

    //Humidity
    $graph = new Graph(600,400);
    $graph->SetScale("textlin");
    $graph->img->SetMargin(40,40,40,40);
    $graph->SetShadow();
    $graph->title->Set("Humitat");
    $graph->xaxis->title->Set("Temps");
    $graph->yaxis->title->Set("Humitat");
    $graph->xaxis->SetTickLabels($datax);
    $bplot = new BarPlot($humx);
    $bplot->SetFillColor("blue");
    $bplot->SetShadow();
    $avg = array_sum($humx)/count($humx);
    $avg = array_fill(0, count($humx), $avg);
    $lineplot=new LinePlot($avg);
    $lineplot->SetColor("red");
    $graph->Add($bplot);
    $graph->Add($lineplot);
    $graph->Stroke("imatges/grafics/humitat.png");

    //Precipitation
    $graph = new Graph(600,400);
    $graph->SetScale("textlin");
    $graph->img->SetMargin(40,40,40,40);
    $graph->SetShadow();
    $graph->title->Set("Precipitació");
    $graph->xaxis->title->Set("Temps");
    $graph->yaxis->title->Set("Precipitació");
    $graph->xaxis->SetTickLabels($datax);
    $bplot = new BarPlot($precipx);
    $bplot->SetFillColor("blue");
    $bplot->SetShadow();
    $avg = array_sum($precipx)/count($precipx);
    $avg = array_fill(0, count($precipx), $avg);
    $lineplot=new LinePlot($avg);
    $lineplot->SetColor("red");
    $graph->Add($bplot);
    $graph->Add($lineplot);
    $graph->Stroke("imatges/grafics/precipitacio.png");

    //Wind speed
    $graph = new Graph(600,400);
    $graph->SetScale("textlin");
    $graph->img->SetMargin(40,40,40,40);
    $graph->SetShadow();
    $graph->title->Set("Velocitat del vent");
    $graph->xaxis->title->Set("Temps");
    $graph->yaxis->title->Set("Velocitat del vent");
    $graph->xaxis->SetTickLabels($datax);
    $bplot = new BarPlot($velx);
    $bplot->SetFillColor("blue");
    $bplot->SetShadow();
    $avg = array_sum($velx)/count($velx);
    $avg = array_fill(0, count($velx), $avg);
    $lineplot=new LinePlot($avg);
    $lineplot->SetColor("red");
    $graph->Add($bplot);
    $graph->Add($lineplot);
    $graph->Stroke("imatges/grafics/velocitat.png");
?>
