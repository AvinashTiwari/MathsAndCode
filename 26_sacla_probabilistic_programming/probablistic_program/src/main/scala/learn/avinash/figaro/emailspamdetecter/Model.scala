package learn.avinash.figaro.emailspamdetecter

import java.util.Dictionary

import com.cra.figaro.language.Element

abstract class Model (val dictionary: Dictionary) {
  val isSpam: Element[Boolean]
  val hasManyUnusualWords : Element[Boolean]
  val numManyUnusualWords: Element[Int]

  val hasWordElements: List[(String, Element[Boolean])]

}
