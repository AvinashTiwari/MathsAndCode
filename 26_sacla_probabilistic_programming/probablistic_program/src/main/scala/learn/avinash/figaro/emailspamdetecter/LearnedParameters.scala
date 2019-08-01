package learn.avinash.figaro.emailspamdetecter

class LearnedParameters(var spamProbability: Double,
                        var hasManyUnusualWordsGivenSpamProbability: Double,
                        var hasManyUnusualWordsGivenNormalProbability: Double,
                        var unusualWordGivenFewProbability: Double,
                        var unusualWordGivenManyProbability: Double,
                        var wordGivenSpamProbabilities: Map[String, Double],
                        var wordGivenNormalProbabilities: Map[String, Double]
                       ) {

}
