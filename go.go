package main

import (
	"encoding/csv"
	"fmt"
	"math"
	"os"
	"strconv"
)

type NaiveBayes struct {
	classCounts map[string]int
	featureCounts map[string]map[string]int
	classProbabilities map[string]float64
	featureProbabilities map[string]map[string]float64
}

func (nb *NaiveBayes) Train(data [][]string) {
	nb.classCounts = make(map[string]int)
	nb.featureCounts = make(map[string]map[string]int)

	for _, record := range data {
		class := record[len(record)-1]
		nb.classCounts[class]++

		for i := 0; i < len(record)-1; i++ {
			feature := "feature" + strconv.Itoa(i)
			value := record[i]

			if nb.featureCounts[feature] == nil {
				nb.featureCounts[feature] = make(map[string]int)
			}
			nb.featureCounts[feature][value]++
		}
	}

	nb.classProbabilities = make(map[string]float64)
	total := len(data)
	for class, count := range nb.classCounts {
		nb.classProbabilities[class] = float64(count) / float64(total)
	}

	nb.featureProbabilities = make(map[string]map[string]float64)
	for feature, counts := range nb.featureCounts {
		nb.featureProbabilities[feature] = make(map[string]float64)
		for value, count := range counts {
			nb.featureProbabilities[feature][value] = float64(count) / float64(nb.classCounts[class])
		}
	}
}

func (nb *NaiveBayes) Predict(record []string) string {
	maxProb := -1.0
	predictedClass := ""

	for class, classProb := range nb.classProbabilities {
		prob := math.Log(classProb)
		for i := 0; i < len(record)-1; i++ {
			feature := "feature" + strconv.Itoa(i)
			value := record[i]
			prob += math.Log(nb.featureProbabilities[feature][value])
		}

		if prob > maxProb {
			maxProb = prob
			predictedClass = class
		}
	}

	return predictedClass
}

func main() {
	file, err := os.Open("preprocessed_data.csv")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer file.Close()

	reader := csv.NewReader(file)
	records, err := reader.ReadAll()
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	nb := NaiveBayes{}
	nb.Train(records)

	// Example prediction
	testRecord := []string{"love", "movie", "great"}
	prediction := nb.Predict(testRecord)
	fmt.Println("Predicted sentiment:", prediction)
}